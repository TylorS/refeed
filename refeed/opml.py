from .common import SandBoxURL, get_auth_headers
import requests


def get_opml(token, url=SandBoxURL):

    return requests.get(url+"/v3/opml",
                        headers=get_auth_headers(token)
                        ).content


def import_opml(token, opml_file, url=SandBoxURL):

    headers = {}
    headers['Content-Type'] = "text/xml"
    headers['Authorization'] = 'OAuth ' + token

    return requests.post(url+"/v3/opml",
                         headers=headers,
                         data=opml_file
                         ).json()
