Things of note:

1. You'll need to have the instances appropriately tagged for instance a key/value pair of TestStartStop/true for the filtering of hosts in the instanceListForLambdaWorker() and instanceNamesForNotification() functions.

2. Make sure you have an IAM Role made when creating the Lambda functions to run, which will have a policy as such associated with it:

	```
	
	{
	    "Version": "2012-10-17",
	    "Statement": [
	        {
	            "Effect": "Allow",
	            "Action": [
	                "logs:CreateLogGroup",
	                "logs:CreateLogStream",
	                "logs:PutLogEvents"
	            ],
	            "Resource": "arn:aws:logs:*:*:*"
	        },
	        {
	            "Effect": "Allow",
	            "Action": [
	                "ec2:Start*",
	                "ec2:Stop*",
	                "ec2:Describe*"
	            ],
	            "Resource": "*"
	        }
	    ]
	}
	
	```


3. You'll need to setup a cron trigger which can be done via an Cloudwatch event/rule based on a schedule, for instance if you want your instances to turn off at 11:59 PM UTC you'd use:

	```
	59 23 ? * mon-fri *
	```

4. You'll need to create a webhook in Slack and use the url in the url variable in slackNotifier().

5. I'm importing boto3, requests and json, though at the time of writing this, requests is not available in the native AWS libraries. To that end, you'll have to package the requests library via pip in a zip with the python program and upload it to Lambda for it to work using something like:

	```
	pip install requests -t /path/to/project-dir
	```

	Note that the `project-dir` is the same place you'll have your Python Lambda function. If you're on OSX also remember to place a `setup.cfg` file in the project-dir with the contents:
	
	```
	[install]
	prefix=
	``` 
6. You can manually invoke Lambda functions to test, for example:
	
	```
	aws lambda invoke --function-name stopEC2instances --invocation-type Event --log-type Tail outputfile.txt
	
	```
