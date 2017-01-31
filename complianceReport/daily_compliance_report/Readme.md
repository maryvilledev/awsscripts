Things of note:

1. Make sure you have an IAM Role made when creating the Lambda function to run, which will have policies as such associated with it:

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
	      "Resource": "*"
	    }
	  ]
	}
	
	```

and

	```
	{
	  "Version": "2012-10-17",
	  "Statement": [
	    {
	      "Effect": "Allow",
	      "Action": [
	        "s3:GetObject"
	      ],
	      "Resource": "arn:aws:s3:::*/AWSLogs/*/Config/*"
	    },
	    {
	      "Effect": "Allow",
	      "Action": [
	        "config:Put*",
	        "config:Get*",
	        "config:List*",
	        "config:Describe*"
	      ],
	      "Resource": "*"
	    }
	  ]
	}
	```

2. You'll need to setup a cron trigger which can be done via an Cloudwatch event/rule based on a schedule, for instance if you want your instances to turn off at 11:59 PM UTC you'd use:

	```
	59 23 ? * mon-fri *
	```

3. You'll need to create a webhook in Slack and use it as the value for the Lambda environment variable `slackHook`.

4. Create a lambda variable `awsRegion` and populate it with the region value to give scope to the lambda function. For example `us-west-2`.

5. Create a lambda variable `slackDestination` and populate it with the intended destination for the Slack notification. For example, in case the recipient is a user you'll use `@john` and if the recipient is a channel you'll use `#BestNotificationChannel`

6. I'm importing boto3, requests and json, though at the time of writing this, requests is not available in the native AWS libraries. To that end, you'll have to package the requests library via pip in a zip with the python program and upload it to Lambda for it to work using something like:

	```
	pip install requests -t /path/to/project-dir
	```

	Note that the `project-dir` is the same place you'll have your Python Lambda function. If you're on OSX also remember to place a `setup.cfg` file in the project-dir with the contents:
	
	```
	[install]
	prefix=
	``` 
7. You can manually invoke Lambda functions to test, for example:
	
	```
	aws lambda invoke --function-name daily-compliance-report-summary --invocation-type Event --log-type Tail outputfile.txt
	
	```