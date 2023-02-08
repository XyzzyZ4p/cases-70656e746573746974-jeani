#!/usr/bin/env python3
import sys
import json
import click

if __package__:
    from .src import parse, State, get_path
else:
    from src import parse, State, get_path

sys.tracebacklimit = 0


@click.command()
@click.argument('json-path', callback=get_path, required=False)
def main(json_path):
    with open(json_path) as fp:
        content = json.load(fp)
    state = State([])
    parse(content, state)
    print(list(state))


if __name__ == '__main__':
    main()
