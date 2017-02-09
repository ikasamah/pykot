# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals
import logging
import requests


class V1Api(object):
    BASE_URL = 'https://api.kingtime.co.jp/v1.0'
    # BASE_URL = 'http://echo.jsontest.com'

    def __init__(self, access_token=None):
        self.log = logging.getLogger('{0.__module__}.{0.__name__}'.format(self.__class__))
        self.access_token = access_token

    def _build_url(self, path):
        return self.BASE_URL + path

    def _default_headers(self):
        return {'Authorization': "Bearer %s" % self.access_token}

    def request(self, path, params=None, method="GET", headers=None):
        url = self._build_url(path)
        self.log.info("{method} {url!r} with params {params!r}".format(method=method, url=url, params=params))

        hdrs = self._default_headers()
        if headers is not None:
            hdrs.update(headers)
        raw = requests.request(method, url, params=params, headers=headers)

        # No Content
        if raw.status_code == 204:
            resp = {}
        else:
            resp = raw.json()

        return resp
