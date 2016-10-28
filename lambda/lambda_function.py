from __future__ import print_function
import json
import boto3
import urllib
import os
import zipfile

print('Loading function')

def lambda_handler(event, context):
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

    print(jsonData['stacks']

    return "Fin."

def check_tmp():
    files = os.listdir('/tmp/')
    for file in files:
        print(file)
