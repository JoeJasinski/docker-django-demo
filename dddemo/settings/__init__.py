try:
    from dddemo.settings.local import *
except ImportError:
    from dddemo.settings.base import *
