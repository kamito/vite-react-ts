#!/usr/bin/env python
import re
import json
import jwt
from base64 import urlsafe_b64encode, urlsafe_b64decode
from urllib.parse import urlparse, parse_qsl, urlencode
from .version import VERSION
from .error import UrlInvalidError, ApiTokenInvalidError


class Blocks:

    def __init__(self, secret=None, api_token=None, auth_token=None):
        self.secret = secret
        self.api_token = api_token if api_token else ""
        self.auth_token = auth_token if auth_token else ""

    def set_login_data(self, data=None):
        self.login_data = data

    def version(self):
        return VERSION

    def api_login(self, email=None, password=None):
        pass

    def redirect_login_url(self, url=None, redirect_to=None):
        if url is None or url == "":
            raise UrlInvalidError()

        auth = self.build_auth()
        u = urlparse(url)
        q = parse_qsl(u.query)
        q.append(('authorization', urlsafe_b64encode(auth.encode())))
        if redirect_to:
            q.append(('redirect_to', redirect_to))
        u = u._replace(query=urlencode(q))
        return u.geturl()

    def build_auth(self):
        api_token = self.api_token if self.api_token else ""
        auth_token = self.auth_token if self.auth_token else ""
        if api_token is None or api_token == "":
            raise ApiTokenInvalidError()

        base_str = "{}:{}".format(self.api_token, self.auth_token)
        auth = urlsafe_b64encode(base_str.encode())
        return "Bearer {}".format(auth.decode())

    def parse_data(self, data=None, verify=True):
        if data is None or data == "":
            return None

        payload = urlsafe_b64decode(data)
        data = jwt.decode(
            payload, self.secret, algorithms=["HS256"],
            options={"verify_signature": verify})
        return data
