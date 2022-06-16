from aws_lambda_powertools import Logger

def handler(event, context):
    for record in event['records']:
        payload = record["body"]

        # this should log the event
        logger = Logger(service=payload)