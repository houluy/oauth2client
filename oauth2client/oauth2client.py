import requests

class OAClient():
    def __init__(self, base_url=None, oauth2_ep=None, auth_ep=None, token_ep=None, **kwargs):
        self.base_url = base_url
        self.oauth2_ep = oauth2_ep
        self.auth_ep = auth_ep
        self.token_ep = token_ep
        self.others = kwargs

    def
