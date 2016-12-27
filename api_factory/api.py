# -*- coding: utf-8 -*-
"""`api_factory.api` module.

Provides the main API class.
"""

import bottle


class API(object):
    """APIFactory API class.
    """

    wsgi_factory = bottle.Bottle

    __slots__ = ('wsgi', 'hooks', 'plugins', 'auth')