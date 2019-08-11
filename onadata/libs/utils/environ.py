import os


class Env:

    def __init__(self, environ=None):
        self.os_environ = environ or os.environ

    def __call__(self, key, default=None, cast=None):
        val = self.os_environ.get(key, default)

        if cast is None or val is None:
            return val

        return cast(val)


