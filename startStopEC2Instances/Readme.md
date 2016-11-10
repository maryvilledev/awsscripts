#Things of note:

1. You'll need to have the instances appropriately tagged for instance a key/value pair of TestStartStop/true for the filtering of hosts in the instanceListForLambdaWorker() and instanceNamesForNotification() functions.

2. You'll need to create a webhook in Slack and use the url in the url variable in slackNotifier().

3. I'm importing boto3, requests and json, though at the time of writing this, requests is not available in the native AWS libraries. To that end, you'll have to package the requests library via pip in a zip with the python program and upload it to Lambda for it to work.
