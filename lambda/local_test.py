import lambda_function

event = {"repository_url": "https://github.com/s-tajima/aws-cfn-lambda-test.git"}
lambda_function.lambda_handler(event, None)
