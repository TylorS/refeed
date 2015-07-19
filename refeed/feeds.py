from .common import SandBoxURL, get_auth_headers
import requests


def get_feed(token, id, url=SandBoxURL):

    return requests.get(url+'/v3/feeds'+id,
                        headers=get_auth_headers(token)
                        )


def get_metadata(token, ids, url=SandBoxURL):

    return requests.get(url+"/v3/feeds/.mget",
                        headers=get_auth_headers(token),
                        params=ids
                        ).json()
