zip:
	(cd lambda && zip -r - *) > lambda.zip
	zip cloudformation.zip *.json
 
test:
	rm -rf /tmp/aws-cfn-lambda-test/
	cd lambda; python local_test.py

up:
	aws s3 cp cloudformation.zip s3://aws-cfn-lambda-test/cloudformation.zip
	aws lambda update-function-code --function-name testFunction --zip-file fileb://lambda.zip
	
