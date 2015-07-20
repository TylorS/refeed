from .common import SandBoxURL, get_auth_headers
import requests


def get_stream_ids(streamId,
                   token="",
                   count=20,
                   ranked="newest",
                   unreadOnly=False,
                   newerThan=0,
                   continuation="",
                   url=SandBoxURL):

    payload = {
      "ranked": ranked,
      "unreadOnly": unreadOnly
    }

    if newerThan > 0:
        payload['newerThan'] = newerThan

    if continuation != "":
        payload['continuation'] = continuation

    return requests.get(
                        url+"/v3/streams/ids?streamId="+streamId,
                        headers=get_auth_headers(token),
                        params=payload
                        ).json()


def get_stream_content(streamId,
                       token="",
                       count=20,
                       ranked="newest",
                       unreadOnly=False,
                       newerThan=0,
                       continuation="",
                       url=SandBoxURL):

    return requests.get(
                        url+"/v3/streams/contents?streamId="+streamId,
                        headers=get_auth_headers(token),
                        params={
                            "count": count,
                            "ranked": ranked,
                            "unreadOnly": unreadOnly,
                            "newerThan": newerThan,
                            "continuation": continuation
                        }
                       ).json()
