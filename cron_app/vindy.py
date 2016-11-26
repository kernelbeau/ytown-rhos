# coding: utf-8
""" """
from lxml import html
import requests


def get_vindy_deaths_daily():
    """ """
    BASE_URL = 'http://www.vindy.com/news/deaths/'

    deaths_daily = dict()
    page = requests.get(BASE_URL)
    tree = html.fromstring(page.content)

    deaths_daily['cur_date'] = tree.xpath('//div[@id="curDate"]/a/text()')

    last_name = tree.xpath('//div[@class="body_text trib_body"]/p/b/text()')
    trib_body = tree.xpath('//div[@class="body_text trib_body"]/p/text()')

    deaths_daily['notice'] = zip(last_name, trib_body)

    return deaths_daily


def format_email_text(deaths_daily):
    """ """
    message = []

    message.append('Youngstown Vindicator - Death Notices')
    message.append(''.join(deaths_daily['cur_date'])+ '\n')
    for name, trib in deaths_daily['notice']:
        message.append('{0} {1}'.format(name, trib.encode('ascii','ignore').strip(' - '))+ '\n')

    return message


def mailgun_send_email(email_text):
    """ """
    BASE_URL = 'https://api.mailgun.net/v3/'
    KEY = 'key-607eb7032024d299077fa0f7ef2d0b0b'
    RECIPIENT = 'julieandlee@yahoo.com'
    SANDBOX = 'sandboxaeec139a4e7a4845ad55e4fab04d4aad.mailgun.org'

    request_url = BASE_URL+ SANDBOX+ '/messages'

    request = requests.post(request_url, auth=('api', KEY), data={
        'from': 'Y-town <mailgun@'+ SANDBOX+ '>',
        'to': RECIPIENT,
        'subject': 'Vindy Deaths - '+ email_text[1].strip(' \n'),
        'text': email_text
    })
    return


if __name__ == "__main__":
    """ """
    deaths_daily = get_vindy_deaths_daily()
    message = format_email_text(deaths_daily)
    mailgun_send_email(message)
