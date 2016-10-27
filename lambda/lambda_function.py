from __future__ import print_function
import json
import boto3

print('Loading function')

def lambda_handler(event, context):
    bn = event['bucket_name']
    path = event['path']

    l = boto3.client('lambda')
    response = l.get_function_configuration(FunctionName=context.function_name)
    print(response['Description'])
    
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(bn, path, '/tmp/' + path)

    return "Fin."
