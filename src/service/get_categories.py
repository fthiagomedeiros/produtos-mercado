
def get_categories():
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

    return body
