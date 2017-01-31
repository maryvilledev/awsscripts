import boto3, json

def lambda_handler(event, context):
     client = boto3.client('ec2')
     message = json.loads(event['Records'][0]['Sns']['Message'])
     if message['newEvaluationResult']['complianceType'] == 'NON_COMPLIANT':
            response = client.create_tags(
                            DryRun=False,
                            Resources=[
                                message['resourceId']
                            ],
                            Tags=[
                                {
                                    'Key': 'tainted',
                                    'Value': 'true'
                                },
                              ]
                            )
     return 