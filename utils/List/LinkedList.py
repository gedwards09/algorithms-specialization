from utils.List.LinkedListNode import LinkedListNode
from utils.List.IList import IList

class LinkedList(IList):

    def __init__(self):
        self._head = None
        self._size = 0

    def __iter__(self):
        current = self._head
        while current != None:
            yield current.get_data()
            current = current.get_next()
    
    def get_head(self):
        return self._head
    
    # Override
    def get_length(self):
        return self._size
    
    # Override
    def get(self, i):
        if i < 0 or i >= self._size:
            raise Exception("LinkedList:get: list index out of range")
        current = self._head
        while i > 0:
            current = current.get_next()
            i -= 1
        return current.get_data()

    # Override
    def set(self, i, data):
        if i < 0 or i >= self._size:
            raise Exception("LinkedList:get: list index out of range")
        current = self._head
        while i > 0:
            current = current.get_next()
            i -= 1
        current.set_data(data)
    
    # Override
    def append(self, data):
        current = self._head
        if current == None:
            self.insert(data)
        else:
            node = self._make_node(data)
            while current != None and current.get_next() != None:
                current = current.get_next()
            current.set_next(node)
    
    def insert(self, data):
        node = self._make_node(data)
        node.set_next(self._head)
        self._head = node
        self._size += 1

    # Private
    def _make_node(self, data):
        return LinkedListNode(data)
    
    def search(self, data):
        current = self._head
        while current != None and data != current.get_data():
            current = current.get_next()
        return current != None
    
    def remove_at(self, i):
        if i < 0 or i >= self._size:
            raise Exception("LinkedList:remove_at: list index out of range")
        if i == 0:
            return self.remove_from_front()
        current = self._head
        while i > 1:
            current = current.get_next()
            i -= 1
        data = current.get_next().get_data()
        current.set_next(current.get_next().get_next())
        self._size -= 1
        return data
    
    def remove_from_front(self):
        if self._size == 0:
            return None
        data = self._head.get_data()
        if self._size == 1:
            self._head = None
        else:
            self._head = self._head.get_next()
        self._size -= 1
        return data
    
    def to_string(self):
        s = ''
        current = self._head
        while current != None:
            s += str(current.get_data())
            s += '->'
            current = current.get_next()
        s += 'null'
        return s
            


    