from .common import SandBoxURL, get_auth_headers
import requests


def get_preferences(token, url=SandBoxURL):

    return requests.get(
                        url+"/v3/preferences",
                        headers=get_auth_headers(token)
                        ).json()


def update_preferences(token, preferences, url=SandBoxURL):

    return requests.post(
                         url+"/v3/preferences",
                         headers=get_auth_headers(token),
                         params=preferences
                         )
