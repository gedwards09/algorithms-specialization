from utils.Stack.IStack import IStack
from utils.List.LinkedList import LinkedList

class LinkedListStack(IStack):

    def __init__(self):
        self._list = LinkedList()

    def __iter__(self):
        if self.has_next():
            yield self.pop()
    
    # Override
    def get_head(self):
        return self._list.get_head()
    
    # Override
    def get_size(self):
        return self._list.get_length()

    # Override
    def push(self, data):
        self._list.insert(data)

    # Override
    def pop(self):
        try:
            return self._list.remove_at(0)
        except:
            raise Exception("Stack:pop: Cannot retrieve node from empty list")

    # Override
    def peek(self):
        if self._list.get_length() == 0:
            raise Exception("Stack:peek: Cannot retrieve node from empty list")
        return self._list.get_head().get_data()
    
    # Override
    def has_next(self):
        return self._list.get_length() > 0