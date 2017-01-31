import boto3, requests, json, os

def configCall(event, context):
    client = boto3.client('config')
    response = client.get_compliance_summary_by_resource_type()
    slackNotifier(response)
    return

def slackNotifier(complianceReport):
    nonCompliantCount = "Number of Non-Compliant Resources:" + str(complianceReport['ComplianceSummariesByResourceType'][0]['ComplianceSummary']['NonCompliantResourceCount']['CappedCount'])
    nonCompliantCapExceeded = "Is the above count capped (max of 100):" + str(complianceReport['ComplianceSummariesByResourceType'][0]['ComplianceSummary']['NonCompliantResourceCount']['CapExceeded'])
    compliantCount = "Number of Compliant Resources:" + str(complianceReport['ComplianceSummariesByResourceType'][0]['ComplianceSummary']['CompliantResourceCount']['CappedCount'])
    compliantCapExceeded = "Is the above count capped (max of 100):" + str(complianceReport['ComplianceSummariesByResourceType'][0]['ComplianceSummary']['CompliantResourceCount']['CapExceeded'])
    configRuleURL = "https://%s.console.aws.amazon.com/config/home?region=%s#/rules/view" % (os.environ['awsRegion'], os.environ['awsRegion'])

    messageText = '*_Daily compliance report for ' + str(os.environ['awsRegion']) + ':_* ' + "\n" + "```" + str(nonCompliantCount) + "\n" + str(nonCompliantCapExceeded) + "\n" + "----------------------------" + "\n" + str(compliantCount) + "\n" + str(compliantCapExceeded) + "\n" + "----------------------------" + "\n" + "For more information visit: " + str(configRuleURL) + "```"
    slackData = {'channel': os.environ['slackDestination'], 'username': 'ComplianceBot', 'text': messageText, 'icon_emoji': ':empire:'}
    url = str(os.environ['slackHook'])
    r = requests.post(url, data=json.dumps(slackData), headers={'Content-Type':'application/json'})


if __name__ == "__main__":
    configCall(None, None)
