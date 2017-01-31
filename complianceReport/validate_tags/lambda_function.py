import json
import boto3

def lambda_handler(event, context):
    print event
    invoking_event = json.loads(event["invokingEvent"])
    rule_parameters = json.loads(event["ruleParameters"])
    
    configuration_item = json.loads(event['invokingEvent'])['configurationItem']
    
    tags = configuration_item['tags']
    compliance = 'COMPLIANT'
    reason = "Resource contains required tags"
    if "CostCenter" not in tags:
        compliance = "NON_COMPLIANT"
        reason = "Resource does not contain required tags"

    result_token = "No token found."
    
    if configuration_item["configurationItemStatus"] == "ResourceDeleted":
        compliance = "NOT_APPLICABLE"
        print "Resource not applicable"
        reason = "Resource not applicable"
        
    if "resultToken" in event:
        result_token = event["resultToken"]

    config = boto3.client("config")
    config.put_evaluations(
        Evaluations=[
            {
                "ComplianceResourceType":
                    configuration_item["resourceType"],
                "ComplianceResourceId":
                    configuration_item["resourceId"],
                "ComplianceType":
                    compliance,
                "Annotation":
                    reason,
                "OrderingTimestamp":
                    configuration_item["configurationItemCaptureTime"]
            },
        ],
        ResultToken=result_token
    )

    
