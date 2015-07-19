from .common import SandBoxURL, get_auth_headers
import requests


def get_all_subscriptions(token, url=SandBoxURL):

    return requests.get(
                        url+"/v3/subscriptions",
                        headers=get_auth_headers(token)
                        ).json()


def add_subscription(token, feed_url, title, categories,
                     url=SandBoxURL):

    return requests.post(
                         url+"/v3/subscriptions",
                         headers=get_auth_headers(token),
                         params={
                            "id": feed_url,
                            "title": title,
                            "categories": categories
                         }
                         ).json()


def update_subscription(token, feed_url, title, categories,
                        url=SandBoxURL):

    return requests.post(
                         url+"/v3/subscriptions",
                         headers=get_auth_headers(token),
                         params={
                            "id": feed_url,
                            "title": title,
                            "categories": categories
                         }
                         ).json()


def update_subscriptions(token, subscriptions, url=SandBoxURL):

    return requests.post(
                         url+"/v3/subscriptions/.mput",
                         headers=get_auth_headers(token),
                         params=subscriptions
                         ).json()


def unsubscribe_from_feed(token, feedId, url=SandBoxURL):

    return requests.delete(
                           url+"/v3/subscriptions/"+feedId,
                           headers=get_auth_headers(token)
                           ).json()


def unsubscribe_from_feeds(token, feeds, url=SandBoxURL):

    return requests.delete(
                           url+"/v3/subscriptions/.mdelete",
                           headers=get_auth_headers(token),
                           params=feeds
                          )
