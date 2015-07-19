import requests
from .common import SandBoxURL, get_auth_headers


# Max count is 20
# Cannot use hours and newerThan at same time
# backFill only used if hours is defined
def get_mix_from_stream(streamID,
                        token="",
                        count=20,
                        unreadOnly=True,
                        hours=0,
                        newerThan=0,
                        backFill=False,
                        locale="",
                        url=SandBoxURL
                        ):
    params = {
        "count": count,
        "unreadOnly": unreadOnly,
        "locale": locale
    }

    if hours > 0:
        params['hours'] = hours
        params['backFill'] = backFill
    else:
        params['newerThan'] = newerThan

    return requests.get(url+"/v3/mixes"+streamID+"/contents",
                        headers=get_auth_headers(token),
                        params=params
                        ).json()
