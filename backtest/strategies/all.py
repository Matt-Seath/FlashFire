import sys
import inspect

from .intraday import *
from .position import *
from .swing import *
from .scalping import *


def get_strategies():
    strategies = {}
    members = inspect.getmembers(sys.modules[__name__], inspect.isclass)

    for member in members:
        short_name = member[1].key
        strategies[short_name] = member[1]

    return strategies
