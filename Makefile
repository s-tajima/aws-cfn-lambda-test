
zip:
	(cd lambda && zip -r - *) > lambda.zip
	zip cloudformation.zip *.json
 
test:
	rm -rf /tmp/aws-cfn-lambda-test/
	cd lambda; python local_test.py

up:
	aws lambda update-function-code --function-name testFunction --zip-file fileb://lambda.zip

travis:
	pip install awscli
	aws lambda invoke --function-name testFunction

