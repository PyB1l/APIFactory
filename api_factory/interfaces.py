# -*- coding: utf-8 -*-
"""`api_factory.interfaces` module.

Provides API definition for APIFactory components.
"""


import abc


class BasePlugin(object, metaclass=abc.ABCMeta):
    """'bottle.py' Plugin API version 2 interface.

    Provides a concrete Plugin Base class for creating bottle.py plugins
    """

    name = None

    api = 2

    def setup(self, app):  # pragma: no cover
        """Make sure that other installed plugins don't affect the same
        keyword argument and check if metadata is available.
        """
        for other in app.plugins:
            if not isinstance(other, self.__class__):
                continue
            if other.keyword == self.keyword:
                raise bottle.PluginError(
                    "Found other plugin registered as {} (non-unique keyword)."
                )

    @abc.abstractmethod
    def apply(self, callback, context):  # pragma: no cover
        pass


class BaseMiddleware(object, metaclass=abc.ABCMeta):
    """BaseMiddleware Abstract class. Provides an interface for creating
    middleware classes that act like proxy-wrappers to the actual bottle
    application instance.

    Subclass BaseMiddleware class and implement `__call__(self, e, h)`
    magic method in order to create an application transparent middleware


    Examples:
        >>> import bottle
        >>>
        ... class MyMiddle(BaseMiddleware):
        ...     def __call__(self, e, h):
        ...         print 'Hi from middleware'
        ...         self.app(e, h)
        ...
        >>> app = MyMiddle(bottle.Bottle())
        >>> print hasattr(app, 'route')
        True
        >>> class MyMw1(BaseMiddleware):
        ...     def __call__(self, e, h):
        ...         print 'Hi from middleware 1'
        ...         self.app(e, h)
        ...
        >>> class MyMw2(BaseMiddleware):
        ...     def __call__(self, e, h):
        ...         print 'Hi from middleware 2'
        ...         self.app(e, h)
        ...
        >>> app = MyMw2(MyMw1(bottle.Bottle()))
        >>> print hasattr(app, 'route')
        True
    """

    def __init__(self, app):
        self.app = app

    def __getattr__(self, attr):
        try:
            return getattr(self.app, attr)
        except AttributeError:  # pragma: no cover
            return None

    def __dir__(self):  # pragma: no cover
        return dir(self.app)

    @abc.abstractmethod
    def __call__(self, e, h):  # pragma: no cover
        pass
