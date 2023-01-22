import sys
import inspect

from .intraday import *
from .position import *
from .swing import *
from .scalping import *


def validate_strategy(strategy):
    strategies = {}
    members = inspect.getmembers(sys.modules[__name__], inspect.isclass)

    for member in members:
        short_name = member[1].key
        strategies[short_name] = member[1]

    if strategy in strategies:
        strategy = strategies[strategy]

        return strategy

    else:
        raise Exception(
            f"Strategy key {strategy} is not associated with any valid strategy")
