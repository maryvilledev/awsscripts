## Description

This is an example of an AWS Lambda consumer function for an AWS Config Rule. If the event/message it receives is an evaluation result, and the result is marked `NON_COMPLIANT`, 
then the function will send a message to the configured Slack endpoint. 

## Preqreqs

You should have an AWS Config Rule set up and it must be publishing evaluation results to an SNS topic. 

You'll need to create a webhook in Slack and use it as the value for the url variable.

It also requires some external dependencies to be installed:

```
pip install -r requirements.txt -t .
```

If you're on OSX also remember to place a `setup.cfg` file in the project-dir with the contents:

```
[install]
prefix=
``` 

## Usage

Because of the external dependency, the Lambda function must be deployed as a zip file. See here for more info: [Creating a Deployment Package (Python)](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)

The Lambda trigger should be set to the SNS queue that the AWS Config rule is publishing to. 