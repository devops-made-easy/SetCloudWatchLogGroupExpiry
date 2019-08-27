import json
import os
import boto3


def lambda_handler(event, context):
    # fetch the environment variable for retention days
    retention = os.environ['RETENTION_DAYS']

    # assign varaibles from event recieved
    log_group_name = event['detail']['requestParameters']['logGroupName']
    region = event['region']

    # form the reponse that will be sent by lambda
    response = f" Updated log group: {log_group_name} retention with {retention} days in region {region}"

    # set the retention policy on log group
    client = boto3.client('logs', region)
    setretention = client.put_retention_policy(
        logGroupName=log_group_name,
        retentionInDays=int(retention)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": response,
            "desc": setretention
            # "location": ip.text.replace("\n", "")
        }),
    }
