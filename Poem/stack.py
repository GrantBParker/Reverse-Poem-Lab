
class Stack:

    def __init__(self):

        self._items = list()

    def __len__(self):

        return len(self._items)

    def peek(self):

        return self._items[-1]

    def pop(self):

        return self._items.pop()

    def push(self, item):

        self._items.append(item)

    def is_empty(self):

        return len(self) == 0
