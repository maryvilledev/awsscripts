import boto3, requests, json

region = 'us-west-2'

def configCall():
    client = boto3.client('config')
    response = client.get_compliance_summary_by_config_rule()

    return response

complianceReport = configCall()

#def lambda_handler(event, context):
#    print 'Daily compliance report: ' + "\n" + str(complianceReport)

print(complianceReport)


#def slackNotifier():
#    messageText = '*_Daily compliance report:_* ' + "\n" + "```" + str(complianceReport) + "```"
#    slackData = {'channel': '@nameOfUser', 'username': 'ComplianceBot', 'text': messageText, 'icon_emoji': ':empire:'}
#    # Replace the value of 'channel' with the name of your channel, 'username' with the name of the bot and the url variable with the actual Slack webhook
#    url = 'https://hooks.slack.com/services/yourSlackEndpoint'
#    r = requests.post(url, data=json.dumps(slackData), headers={'Content-Type':'application/json'})

#slackNotifier()