import requests
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from urllib.parse import urlparse, parse_qs

from refeed.common import(
    client_id,
    client_secret,
    SandBoxURL,
    oauth2_redirect,
    scope,
    headers)

API_URL = SandBoxURL + '/v3/auth'


class FeedlyClient():

    def __init__(self):
        super().__init__()

    def parse_code(self):
        if oauth2_redirect in self.engine.url().toString():
            self.webview.close()
            parse = parse_qs(urlparse(self.engine.url().toString()).query)
            self.code = parse['code']
            self.app.exit()

    def obtain_code(self, url=API_URL+'/auth', state=""):

        self.app = QApplication([])

        payload = {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": oauth2_redirect,
            "scope": scope,
            "state": state
        }

        res = requests.get(url, params=payload, headers=headers)
        self.webview = QMainWindow()

        self.engine = QWebEngineView()
        self.engine.setUrl(QUrl(res.url))
        self.engine.urlChanged.connect(self.parse_code)

        self.webview.setCentralWidget(self.engine)
        self.webview.show()
        self.app.exec_()

    def get_access_token(self, url=API_URL+"/token", state=''):

        payload = {
            'code': self.code,
            'client_id': client_id,
            'client_secret': client_secret,
            'redirect_uri': oauth2_redirect,
            'state': state,
            'grant_type': 'authorization_code'
        }

        res = requests.post(url,
                            params=payload,
                            headers=headers).json()

        self.refresh_token = res['refresh_token']
        self.id = res['id']
        self.plan = res['plan']
        self.state = res['state']
        self.token_type = res['token_type']
        self.access_token = res['access_token']
        self.expires_in = res['expires_in']

    def get_refresh_token(self, url=API_URL+"/token", state=''):

        payload = {
            'refresh_token': self.refresh_token,
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'refresh_token'
        }

        res = requests.post(url,
                            params=payload,
                            headers=headers).json()

        self.id = res['id']
        self.access_token = res['access_token']
        self.expires_in = res['expires_in']
        self.token_type = res['token_type']
        self.plan = res['plan']