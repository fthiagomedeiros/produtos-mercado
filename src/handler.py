import json

from src.service.service import get_categories, create_new_list


def create_list(event, context):
    body = create_new_list()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
        # "event": json.dumps(event)
    }

    return response


def hello(event, context):
    body = get_categories()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
        # "event": json.dumps(event)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


def post_category(event, context):
    body = json.loads(event)

    response = {
        "statusCode": 200,
        "body": body
    }

    return response
