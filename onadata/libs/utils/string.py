from distutils.util import strtobool


def str2bool(v):
    return v.lower() in (
        'yes', 'true', 't', '1') if isinstance(v, basestring) else v


def sbool(txt):
    if isinstance(txt, bool):
        return txt
    return bool(strtobool(txt))
