## Description

This is an example of an AWS Lambda consumer function for an AWS Config Rule. If the event/message it receives is an evaluation result, the function
will tag the resources with `tainted=true`. The tagged resources could then be dealt with accordingly, e.g. stopped/deleted by another Lambda function.  

## Usage

The Lambda trigger should be set to the SNS queue that the AWS Config rule is publishing to. 

The role for this function requires privileges for tagging ec2 resources. 

Example policy for tagging ec2 resources:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1485810506000",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags",
                "ec2:DeleteTags"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```