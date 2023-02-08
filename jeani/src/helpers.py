import os
import errno
import click
from typing import Any
from pathlib import Path


def get_path(ctx: Any, param: Any, value: Any) -> str:
    if not value and not click.get_text_stream('stdin').isatty():
        value = click.get_text_stream('stdin').read().strip()
    try:
        path = Path(value)
    except TypeError as e:
        raise FileNotFoundError(os.strerror(errno.ENOENT)) from None
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(os.strerror(errno.ENOENT))
    return value


__all__ = ('get_path',)
