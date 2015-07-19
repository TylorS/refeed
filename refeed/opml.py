from .common import SandBoxURL, get_auth_headers
import requests


def get_opml(token, url=SandBoxURL):

    return requests.get(url+"/v3/opml",
                        headers=get_auth_headers(token)
                        ).json()


def import_opml(token, opml_file, url=SandBoxURL):

    return requests.post(url+"/v3/opml",
                         headers=get_auth_headers(token),
                         files={'file': open(opml_file, 'rb')}
                         ).json()
