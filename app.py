from aws_lambda_powertools import Logger

logger = Logger(service="JPC-Messaging-Service")

@logger.inject_lambda_context(log_event=True)
def handler(event, context):
    for record in event['records']:
        payload = record["body"]
        logger.info({"record": payload})
