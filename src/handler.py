import json


def hello(event, context):
    body = {
        "categories": [
            {
                "category_id": 1000,
                "category_name": "laticinios",
                "category_items": [
                    {
                        "id": 1001,
                        "name": "leite"
                    },
                    {
                        "id": 1002,
                        "name": "queijo"
                    }
                ]
            },
            {
                "category_id": 2000,
                "category_name": "padaria",
                "category_items": [
                    {
                        "id": 2001,
                        "name": "pao"
                    },
                    {
                        "id": 2002,
                        "name": "biscoito"
                    }
                ]
            }
        ]
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
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
