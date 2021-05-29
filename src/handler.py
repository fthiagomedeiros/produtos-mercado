import json

from src.service.service import create_new_list


def create_list(event, context):
    owner_id = json.loads(event['body'])['owner-id']
    owner_name = json.loads(event['body'])['owner-name']
    body = create_new_list(owner_id, owner_name)

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "event": json.dumps(event)
    }

    return response