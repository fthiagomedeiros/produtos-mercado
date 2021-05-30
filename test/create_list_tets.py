import unittest

from src.handler import create_list

event = {
    "body": "{ \"owner-email\":\"fthiagomedeiros@gmail.com\", \"owner-name\":\"Francisco\", \"to-buy\": {\"arroz\": 5, \"feijao\": 3}, \"not-to-buy\": [\"manteiga\", \"amaciante\", \"frango\"]}\n",
    "resource": "/{proxy+}",
    "path": "/path/to/resource",
    "httpMethod": "POST",
    "queryStringParameters": {
        "foo": "bar"
    },
    "pathParameters": {
        "proxy": "path/to/resource"
    },
    "stageVariables": {
        "baz": "qux"
    },
    "requestContext": {
        "accountId": "123456789012",
        "resourceId": "123456",
        "stage": "prod",
        "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
        "resourcePath": "/{proxy+}",
        "httpMethod": "POST",
        "apiId": "1234567890"
    }
}


class Context:
    aws_request_id = 111


class MyTestCase(unittest.TestCase):

    def test_creates_new_list(self):
        context = Context()
        handler = create_list(event, context)
        assert handler is not None


if __name__ == '__main__':
    unittest.main()
