from .common import SandBoxURL, get_auth_headers
import requests


def search_for_feeds(query, count=20, locale="", token="", url=SandBoxURL):

    return requests.get(url+"/v3/search/feeds",
                        params={
                            "query": query,
                            "count": count,
                            "locale": locale
                        },
                        headers=get_auth_headers(token)
                        ).json()


def search_content_of_stream(token,
                             query,
                             streamId,
                             count=20,
                             newerThan=0,
                             continuation="",
                             fields="all",
                             embedded="",
                             engagement="",
                             locale="",
                             url=SandBoxURL):

    return requests.get(url+"/v3/search/"+streamId,
                        headers=get_auth_headers(token),
                        params={
                            "query": query,
                            "count": count,
                            "newerThan": newerThan,
                            "continuation": continuation,
                            "fields": fields,
                            "embedded": embedded,
                            "engagement": engagement,
                            "locale": locale
                        }).json()
