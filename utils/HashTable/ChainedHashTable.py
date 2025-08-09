from utils.HashTable.ArrayBackedHashTable import ArrayBackedHashTable
from utils.List.LinkedList import LinkedList

class ChainedHashTable(ArrayBackedHashTable):
    
    # Override
    def add(self, data):
        h = self.hash(data)
        self._add(data, h)
    
    # Internal
    # Override
    def _add(self, data, h):
        if self._get_at(h) == None:
            self._set_at(h, self.make_list())
        if not self._lookup(data, h):
            self._get_at(h).insert(data)
        self._increment_size()

    def make_list(self):
        return LinkedList()
    
    # Internal
    # Override
    def _lookup(self, data, h):
        if self._get_at(h) == None:
            return False
        return self._get_at(h).search(data)

    # Override
    def lookup(self, data):
        h = self.hash(data)
        return self._lookup(data, h)
    
    # Override
    def iterate_data(self, key):
        ls = self._get_at(key)
        if ls != None:
            for el in ls:
                yield el