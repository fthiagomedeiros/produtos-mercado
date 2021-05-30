import json

from src.service.service import create_new_list


def create_list(event, context):

    owner_id = json.loads(event['body'])['owner-email']
    owner_name = json.loads(event['body'])['owner-name']
    to_buy = json.loads(event['body'])['to-buy']
    not_to_buy = json.loads(event['body'])['not-to-buy']

    body = create_new_list(context.aws_request_id,
                           owner_id,
                           owner_name,
                           to_buy,
                           not_to_buy)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
