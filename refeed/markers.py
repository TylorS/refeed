from .common import SandBoxURL, get_auth_headers, get_time
import requests


def get_unread_counts(token, newerThan,
                      auto_refresh=False,
                      streamId="",
                      url=SandBoxURL):
    return requests.get(url+'/v3/markers/counts',
                        headers=get_auth_headers(token),
                        params={
                            "autorefresh": auto_refresh,
                            "newerThan": newerThan,
                            "streamId": streamId
                        }).json()


def mark_entries_read(token, entries, url=SandBoxURL):

    return requests.post(url+'/v3/markers',
                         headers=get_auth_headers(token),
                         params={
                             "action": "markAsRead",
                             "type": "entries",
                             "entryIds": entries
                         }).json()


def mark_entries_unread(token, entries, url=SandBoxURL):

    return requests.post(url+'/v3/markers',
                         headers=get_auth_headers(token),
                         params={
                             "action": "markUnread",
                             "type": "entries",
                             "entryIds": entries
                         }).json()


def mark_feeds_read(token, feeds, url=SandBoxURL, asOf=False):

    if asOf:
        return requests.post(url+'/v3/markers',
                             headers=get_auth_headers(token),
                             params={
                                 "action": "markAsRead",
                                 "type": "feeds",
                                 "feedIds": feeds,
                                 "asOf": get_time()
                             }).json()
    else:
        return requests.post(url+'/v3/markers',
                             headers=get_auth_headers(token),
                             params={
                                 "action": "markAsRead",
                                 "type": "feeds",
                                 "feedIds": feeds
                             }).json()


def mark_categories_read(token, categories, url=SandBoxURL, lastRead=None):

    if lastRead is not None:
        return requests.post(url+'/v3/markers',
                             headers=get_auth_headers(token),
                             params={
                                "action": "markAsRead",
                                "type": "categores",
                                "categoryIds": categories,
                                "lastReadEntryId": lastRead
                             }).json()
    else:
        return requests.post(url+'/v3/markers',
                             headers=get_auth_headers(token),
                             params={
                                "action": "markAsRead",
                                "type": "categores",
                                "categoryIds": categories,
                                "asOf": get_time()
                             }).json()


def undo_mark_as_read(token, type, type_ids, url=SandBoxURL):

    params = {
        "action": "undoMarkAsRead",
        "type": type
    }

    if type is "feeds":
        params['feedIds'] = type_ids
    if type is "categories":
        params['categoryIds'] = type_ids
    if type is "entries":
        params['entryIds'] = type_ids

    return requests.post(url+'/v3/markers',
                         headers=get_auth_headers(token),
                         params=params
                         ).json()


def mark_as_saved(token, type, type_ids, url=SandBoxURL):

    params = {
        "action": "markAsSaved",
        "type": type
    }

    if type is "feeds":
        params['feedIds'] = type_ids
    if type is "categories":
        params['categoryIds'] = type_ids
    if type is "entries":
        params['entryIds'] = type_ids

    return requests.post(url+'/v3/markers',
                         headers=get_auth_headers(token),
                         params=params
                         ).json()


def mark_unsaved(token, type, type_ids, url=SandBoxURL):

    params = {
        "action": "markAsUnsaved",
        "type": type
    }

    if type is "feeds":
        params['feedIds'] = type_ids
    if type is "categories":
        params['categoryIds'] = type_ids
    if type is "entries":
        params['entryIds'] = type_ids

    return requests.post(url+'/v3/markers',
                         headers=get_auth_headers(token),
                         params=params
                         ).json()


def get_reads(token, newerThan, url=SandBoxURL):

    return requests.get(url+'/v3/markers/reads',
                        params={
                            "newerThan": newerThan
                        },
                        headers=get_auth_headers(token)
                        ).json()


def get_tags(token, newerThan, url=SandBoxURL):

    return requests(url++'/v3/markers/tags',
                    params={
                        "newerThan": newerThan
                    },
                    headers=get_auth_headers(token)
                    ).json()
