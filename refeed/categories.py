import requests
from .common import SandBoxURL, get_auth_headers


def get_all_categories(token, url=SandBoxURL):
    """
    Get all of the categories for a user

    :param token: An Access Token
    :param url: Base Url to call API from (default https://sandbox.feedly.com)
    """
    return requests.get(url+'/v3/categories',
                        headers=get_auth_headers(token)
                        ).json()


def change_category_label(token, id, label, url=SandBoxURL):
    """
    Change Label of a category

    :param token: An Access Token
    :param id: ID of the Category you would like to change
    :param label: New label for the Category
    :param url: Base Url to call API from (default https://sandbox.feedly.com)
    """

    payload = {
        "label": label
    }

    return requests.post(url+'/v3/categories/'+id,
                         params=payload,
                         headers=get_auth_headers(token)
                         ).json()


def delete_category(token, id, url=SandBoxURL):
    """
    Get all of the categories for a user

    :param token: An Access Token
    :param id: ID of category you would like to delete
    :param url: Base Url to call API from (default https://sandbox.feedly.com)
    """

    return requests.delete(url+'/v3/categories/'+id,
                           headers=get_auth_headers(token)
                           ).json()
