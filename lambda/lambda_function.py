from __future__ import print_function

import json
import git

print('Loading function')

def lambda_handler(event, context):
    print("repository_url = " + event['repository_url'])

    git.Repo.clone_from(event['repository_url'], '/tmp/', branch='master')
    return event['repository_url']

event = {"repository_url": "https://github.com/s-tajima/aws-cfn-lambda-test.git"}
lambda_handler(event, None)