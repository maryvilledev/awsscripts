Sample lambda functions for AWS Config rules. 

 - *validate_tags*: To be used as a custom AWS Config rule. Validates the presence of specific tags on EC2 resources. 
 - *compliance_tags*: Listens to SNS topic that Config rule publishes to, adds "tainted=true" tag to resources marked as NON_COMPLIANT by AWS Config rule.
 - *compliance_notification*: Listens to SNS topic that Config rule publishes to, sends slack message when NON_COMPLIANT resources are detected.
 - *daily_compliance_report*: Can be set to run on a CloudWatch even (cron) to give current status of resource compliance. Depends on Config Rules to have been created and run, with up to date evaluations.