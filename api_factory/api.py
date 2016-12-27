# -*- coding: utf-8 -*-
"""`api_factory.api` module.

Provides API class.
"""

import bottle


class API(object):
    """
    """

    wsgi_factory = bottle.Bottle

    __slots__ = ('wsgi', 'hooks', 'plugins', 'auth')


    def __init__(self, hooks, plugins):
        self.wsgi = self.wsgi_factory()