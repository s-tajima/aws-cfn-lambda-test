from __future__ import print_function
import git
import json
import boto3

print('Loading function')

def lambda_handler(event, context):
    
    print("repository_url = " + event['repository_url'])

    git.Repo.clone_from(event['repository_url'], '/tmp/aws-cfn-lambda-test/', branch='master')

    client = boto3.client('lambda')
    response = client.get_function_configuration(FunctionName=context.function_name)
    print(response['Description'])

    return event['repository_url']
