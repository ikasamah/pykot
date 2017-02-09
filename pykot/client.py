# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals
import logging

from pykot.api import Api


class Client(object):

    def __init__(self, access_token=None):
        self.log = logging.getLogger('{0.__module__}.{0.__name__}'.format(self.__class__))
        self.api = Api(access_token)

    @property
    def access_token(self):
        return self.api.access_token

    @access_token.setter
    def access_token(self, v):
        self.api.access_token = v

    def get_employees(self):
        raise NotImplementedError

    def get_employee(self, code, date=None, additional_fields=None):
        raise NotImplementedError

    # TODO: Add extra methods

    def request(self, path, **kwargs):
        """
        for test
        """
        return self.api.request(path, kwargs)
