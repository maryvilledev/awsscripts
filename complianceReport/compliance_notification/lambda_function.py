import json, httplib, requests


def lambda_handler(event, context):
    # print json.dumps(event)
    message = json.loads(event['Records'][0]['Sns']['Message'])


    if 'newEvaluationResult' in message:
        if message['newEvaluationResult']['complianceType'] == 'NON_COMPLIANT':
            print "Calling slack"
            slackNotifier(buildMessageText(message))

    return


def slackNotifier(messageText):
    slackData = {'username': 'AWS Config Compliance Checker', 'text': messageText}
    # Replace the value of 'channel' with the name of your channel, 'username' with the name of the bot and the url variable with the actual Slack webhook
    url = 'https://hooks.slack.com/services/your/service/hook'
    
    r = requests.post(url, data=json.dumps(slackData), headers={'Content-Type':'application/json'})
    
def buildMessageText(message):
    configUrl = "https://%s.console.aws.amazon.com/config/home?region=%s#/rules/rule-details/%s" % (message['awsRegion'], message['awsRegion'], message['configRuleName'])
    
    messageText = "*Non Compliant Resource Detected*: \n \n The following resource failed to comply with AWS Config rule `%s`:\n\
ResourceType: `%s` \n ResourceId: `%s` \n Reason: `%s` \n \n Details: \n %s" % \
    (message['configRuleName'], message['resourceType'], message['resourceId'], message['newEvaluationResult']['annotation'], configUrl )
    
    return messageText