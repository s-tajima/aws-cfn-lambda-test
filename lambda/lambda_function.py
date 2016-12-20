from __future__ import print_function
from pprint import pprint
import json
import boto3
import urllib
import os
import zipfile

print('Loading function')

def lambda_handler(event, context):
    pprint(event)

    l = boto3.client('lambda')
    response = l.get_function_configuration(FunctionName=context.function_name)
    print(response['Description'])
    
    url = 'https://github.com/s-tajima/aws-cfn-lambda-test/archive/master.zip'
    urllib.urlretrieve(url, '/tmp/master.zip')

    check_tmp()

    zip_ref = zipfile.ZipFile('/tmp/master.zip', 'r')
    zip_ref.extractall('/tmp/')
    zip_ref.close()

    check_tmp()

    f = open('/tmp/aws-cfn-lambda-test-master/stacklist.json', 'r')
    jsonData = json.load(f)
    f.close()


    cloudformation = boto3.client('cloudformation')
    exist_stacks = cloudformation.list_stacks()['StackSummaries']

    print(exist_stacks)

    for stack in jsonData['stacks']:
        print(stack['stack_name'])
        print(stack['template_path'])

        template = open('/tmp/aws-cfn-lambda-test-master/' + stack['template_path'], 'r')
        new_template_json = template.read()
        new_template_dict = json.loads(new_template_json)

        if len(filter(lambda x: x['StackName'] == stack['stack_name'], exist_stacks)) == 0:
            print("Stack " + stack['stack_name'] + " is not exists.")
            print("CreateStack ...")
            cloudformation.create_stack( StackName=stack['stack_name'], TemplateBody=new_template_json )
            next

        current_template = cloudformation.get_template( StackName=stack['stack_name'] )['TemplateBody']
        if current_template == new_template_dict:
            print("Template is not updated.")
            next

        change_sets = cloudformation.list_change_sets( StackName=stack['stack_name'] )['Summaries']
        pprint(change_sets)

        if event["TRAVIS_EVENT_TYPE"] == "pull_request":
            for change_set in change_sets:
                cloudformation.delete_change_set( ChangeSetName=change_set["ChangeSetId"] )

            print("Stack " + stack['stack_name'] + " is already exists.")
            print("CreateChangeSet ...")
            cloudformation.create_change_set( StackName=stack['stack_name'], TemplateBody=new_template_json, ChangeSetName=stack['stack_name'] + "-" + event["TRAVIS_PULL_REQUEST"] )
            next

    return "Fin."

def check_tmp():
    files = os.listdir('/tmp/')
    for file in files:
        print(file)
