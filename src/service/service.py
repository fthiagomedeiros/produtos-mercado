categories = {
    "laticinios": [
                {
                    "id": 1001,
                    "name": "leite"
                },
                {
                    "id": 1002,
                    "name": "queijo"
                }
            ],

    "padaria": [
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


def get_categories():
    """
    get list of categories
    :return: the categories list
    """
    return categories


def create_category(category_name, category_items):
    """
    Creating a new category and items
    :param category_name: the category name
    :param category_items: the items in the category in following format below
                {
                    "id": 2001,
                    "name": "pao"
                }
    :return: a newly created category
    """

    categories[category_name] = category_items

    return categories
