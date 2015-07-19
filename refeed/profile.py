from .common import SandBoxURL, get_auth_headers
import requests


def get_profile(token, url=SandBoxURL):

    return requests.get(url+"/v3/profile",
                        headers=get_auth_headers(token)).json()


def update_profile(token, profile, url=SandBoxURL):

    return requests.post(url+"/v3/profile",
                         params=profile,
                         headers=get_auth_headers(token)
                         ).json()
