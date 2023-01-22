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
        strategy_object = strategies[strategy]

        return strategy_object

    else:
        raise Exception(
            f"The strategy key provided ({strategy.upper()}) is not associated with any valid strategy")
