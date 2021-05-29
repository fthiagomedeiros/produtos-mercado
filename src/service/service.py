categories = {
    "id": 100,
    "owner_name": "Francisco Medeiros",
    "owner_email": "fthiagomedeiros@gmail.com",
    "shared_name": "-",
    "shared_email": "-",
    "items_enabled": [
        {
            "category": "higiene",
            "description": "Pasta de Dentes"
        }
    ],
    "items_disabled": [
        {
            "category": "carnes",
            "description": "Fraldinha"
        }
    ]
}

shopping_lists = {}


def create_new_list(owner_id, owner_name):
    shopping_lists['id'] = owner_id
    shopping_lists['name'] = owner_name
    return shopping_lists


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
