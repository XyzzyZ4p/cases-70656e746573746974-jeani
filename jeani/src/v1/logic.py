from typing import Sequence
from collections.abc import Iterable

from ..state import State


def parse(data: Sequence, state: State) -> None:
    if isinstance(data, Iterable) and not isinstance(data, str):
        if isinstance(data, dict):
            for k, v in data.items():
                parse(k, state)
                parse(v, state)
        else:
            for item in data:
                parse(item, state)
    elif data not in state:
        state.append(data)


__all__ = ('parse',)
