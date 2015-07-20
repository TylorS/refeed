import os
from time import time
from decimal import Decimal

client_id = os.getenv("FEEDLY_CLIENT_ID")
client_secret = os.getenv("FEEDLY_CLIENT_SECRET")
oauth2_redirect = os.getenv("FEEDLY_REDIRECT_URI")

SandBoxURL = 'https://sandbox.feedly.com'
CloudURL = 'https://cloud.feedly.com'

scope = "https://cloud.feedly.com/subscriptions"

headers = {
    "Content-Type": "application/json"
}


def get_auth_headers(token):
    """
    Get Headers for a request

    :param token: An access token
    :returns: Dict with Content-Type and Authorization Headers
    """
    headers = {}
    headers['Content-Type'] = "application/json"
    headers['Authorization'] = 'OAuth ' + token

    return headers


def get_time():
    """
    Get the current time in milliseconds rounded
    to a whole number.
    """
    return str(Decimal(time()).to_integral_exact())
