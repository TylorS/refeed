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

	headers = {}
	headers['Content-Type'] = "application/json"
	headers['Authorization'] = 'OAuth ' + token

	return headers

def get_time():
	return str(Decimal(time()).to_integral_exact())