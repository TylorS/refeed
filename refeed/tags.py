from .common import SandBoxURL, get_auth_headers
import requests


def get_all_tags(token, url=SandBoxURL):

    return requests.get(url+"/v3/tags", headers=get_auth_headers(token))


def tag_entries(token, entries, tags, url=SandBoxURL):

    return requests.get(
                        url+"/v3/tags"+str(','.join(tags)),
                        headers=get_auth_headers(token),
                        params={"entryIds": entries}
                        ).json()


def change_tag_label(token, tagId, label, url=SandBoxURL):

    return requests.post(url+"/v3/tags/"+tagId,
                         headers=get_auth_headers(token),
                         params={"label": label}
                         ).json()


def untag_entries(token, tags, entries, url=SandBoxURL):

    tags = ','.join(tags)
    entries = ','.join(entries)

    return requests.delete(
                           url+"/v3/tags"+tags+"/"+entries,
                           headers=get_auth_headers(token)).json()


def delete_tags(token, tags, url=SandBoxURL):

    return requests.delete(url+"/v3/tags"+str(','.join(tags)),
                           headers=get_auth_headers(token)).json()
