import boto3, requests, json

# Enter the region your instances are in, e.g. 'us-east-1'

region = 'us-west-2'

def instanceListForLambdaWorker():
    client = boto3.client('ec2')
    instanceDict=client.describe_instances(
        Filters=[{'Name':'tag:TestStartStop','Values':['true']}]
        # replace the tag TestStartStop and it's true value with whatever tage you'd like to filter the instances down to
        )

    hostList=[]
    for r in instanceDict['Reservations']:
        for inst in r['Instances']:
            hostList.append(inst['InstanceId'])
    return hostList


instances = instanceListForLambdaWorker()

def instanceNamesForNotification():
    client = boto3.client('ec2')
    instanceDict=client.describe_instances(
        Filters=[{'Name':'tag:TestStartStop','Values':['true']}]
        # replace the tag TestStartStop and it's true value with whatever tage you'd like to filter the instances down to
        )
    
    hostTags=[]
    for r in instanceDict['Reservations']:
        for inst in r['Instances']:
            for tags in inst['Tags']:
                if tags['Key'] == 'Name': 
                    hostTags.append(tags['Value'] + " : " + inst['InstanceId'])
                    
    finalList = ("\n".join(hostTags))
    return finalList               

instanceNames = instanceNamesForNotification()

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print 'Started your instances: ' + str(instanceNames)
    

def slackNotifier():
    messageText = '*_Started your instances:_* ' + "\n" + str(instanceNames)
    slackData = {'channel': '#NameOfChannel', 'username': 'NameOfBot', 'text': messageText, 'icon_emoji': ':sunny:'}
    # Replace the value of 'channel' with the name of your channel, 'username' with the name of the bot and the url variable with the actual Slack webhook
    url = 'https://hooks.slack.com/services/IdentifierForYourWebhook'
    r = requests.post(url, data=json.dumps(slackData), headers={'Content-Type':'application/json'})

slackNotifier()
