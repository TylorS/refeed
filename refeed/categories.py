import requests
from .common import SandBoxURL, get_auth_headers


def get_all_categories(token, url=SandBoxURL):

    return requests.get(url+'/v3/categories',
                        headers=get_auth_headers(token)
                        ).json()


def change_category_label(token, id, label, url=SandBoxURL):

    payload = {
        "label": label
    }

    return requests.post(url+'/v3/categories'+id,
                         params=payload,
                         headers=get_auth_headers(token)
                         ).json()


def delete_category(token, id, url=SandBoxURL):

    return requests.delete(url+'/v3/categories'+id,
                           headers=get_auth_headers(token)
                           ).json()
