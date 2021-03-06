zip:
	(cd lambda && zip -r - *) > lambda.zip
	zip cloudformation.zip *.json
 
test:
	rm -rf /tmp/aws-cfn-lambda-test/
	cd lambda; python local_test.py

up:
	aws lambda update-function-code --function-name testFunction --zip-file fileb://lambda.zip


setup:
	pip install --user awscli

invoke:
	aws lambda invoke --function-name testFunction --payload "{\"TRAVIS_EVENT_TYPE\":\"${TRAVIS_EVENT_TYPE}\", \"TRAVIS_PULL_REQUEST\":\"${TRAVIS_PULL_REQUEST}\" }" /tmp/outfile.txt
	cat /tmp/outfile.txt

travis_env:
	echo $(TRAVIS_BRANCH)

travis: travis_env setup invoke
