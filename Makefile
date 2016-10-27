zip:
	(cd lambda && zip -r - *) > lambda.zip

test:
	rm -rf /tmp/aws-cfn-lambda-test/
	cd lambda; python local_test.py
	
