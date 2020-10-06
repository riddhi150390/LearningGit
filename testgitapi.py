import os
import json
import requests
from github import Github
from zenhub import Zenhub

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
GIT_LABEL = 'ZENHUB'
USERNAME = 'erridzzi@gmail.com'
PASSWORD = 'Github@123456789'
zenhubtoken = 'bbf133e252d9044a133c77570e4e55299d658dc30905f5453ecd1b7c06a4857682fe450fca9bc72a'
zh = Zenhub(zenhubtoken)
z = zh.get_epics(295388926)

for j in range(1,7): 
     i = zh.get_issue_data(295388926,j)
#print (z)
     k = json.dumps(i)
     print(k.pipelines)

"""
# The repository to add this issue to

print ('step 1:')

def make_github_issue(title,body,labels):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/riddhi150390/LearningGit/issues'
    url1 ='https://api.zenhub.com/'
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    print (title)
    print (body)
   
    issue = {'title': title,
             'body': body, 
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    print ('Step 2:')
    print (r)
    print (r.status_code)
    if r.status_code == 201:
        print ('Successfully created Issue {0:s}'.format(title))
#   else:
#       print ('Could not create Issue {0:s}'.format(title)
#	print ('Response:', r.content)
    print('**********')
    params = {
     	    #"state": "open",
            "labels" : "ZENHUB"
            }
    openissue = requests.get(url,params=params)
    #openissue.json() > text.html
    print(openissue.json())
"""

"""
   repo = Github.get_repo("riddhi150390/LearningGit")
    issues = repo.get_issues(state="open")
    print(issues.get_page(0))
"""


"""
make_github_issue("Zenhub integration testing","kindly complete this as soon as possible--body",labels=[GIT_LABEL])
#make_github_issue(title,body,labels)
"""
