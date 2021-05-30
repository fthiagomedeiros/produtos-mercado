shopping_lists = {}


def save_list(owner_email, shopping_list):
    if owner_email in shopping_lists.keys():
        shopping_lists[owner_email].append(shopping_list)
    else:
        shopping_lists[owner_email] = []
        shopping_lists[owner_email].append(shopping_list)


def create_new_list(id, owner_email, owner_name, items_to_buy=None, items_not_to_buy=None):

    if items_not_to_buy is None:
        items_not_to_buy = []
    if items_to_buy is None:
        items_to_buy = {}

    shopping_list = {'list-id': id,
                     'owner-email': owner_email,
                     'owner-name': owner_name,
                     'to-buy': items_to_buy,
                     'not-to-buy': items_not_to_buy}

    save_list(owner_email, shopping_list)

    return shopping_lists
