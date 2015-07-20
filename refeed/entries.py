from .common import SandBoxURL, get_auth_headers
import requests


def get_entry_content(entryId, token="", url=SandBoxURL):

    return requests.get(url+"/v3/entries/"+entryId,
                        headers=get_auth_headers(token)).json()


def get_entries_content(entries, token="", url=SandBoxURL):

    return requests.get(url+"/v3/entries/.mget",
                        headers=get_auth_headers(token),
                        params=entries)


# I don't understand the documentation on this yet
def create_and_tag_entry():
    return "This doesn't work just yet"
