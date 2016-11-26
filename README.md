# ytown-rhos
Flask app in OpenShift

Create Python application:

`$ rhc app create ytown python-2.7`

Add Flask and other dependencies to requirements.txt:
'''
Flask==0.11.1

lxml==3.6.4*

requests==2.12.1

* lxml would not install with pip. ssh into account and install with easy_install
'''

Clone this git repo to your local machine:

`$ git clone https://github.com/kernelbeau/ytown`

Add the openshift repo as remote to the clone:

`$ git remote add openshift -f <openshift-git-repo-url>`

Merge the openshift repo with the local clone:

`$ git merge openshift/master -s recursive -X ours`

Push the git repo to openshift:

`$ git push openshift HEAD`

When needed push the local clone to github:
`$ git push origin master`
