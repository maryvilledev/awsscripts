Sample lambda functions for AWS Config rules. 

 - *validate_tags*: to be used as a custom AWS Config rule. Validates the presence of specific tags on EC2 resources. 
 - *compliance_tags*: listens to SNS topic that Config rule publishes to, adds "tainted=true" tag to resources marked as NON_COMPLIANT by AWS Config rule.
 - *compliance_notification*: listens to SNS topic that Config rule publishes to, sends slack message when NON_COMPLIANT resources are detected. 
