from collections import UserList


class State(UserList):
    def __init__(self, iterable):
        super().__init__(iterable)


__all__ = ('State',)
