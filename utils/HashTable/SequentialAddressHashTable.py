from math import floor, sqrt
from utils.HashTable.ArrayBackedHashTable import ArrayBackedHashTable

#
# Implements linear probing for array backed hash table
#
class SequentialAddressHashTable(ArrayBackedHashTable):

    # Override
    def add(self, data):
        h = self.hash(data)
        self._add(data, h)

    # Internal
    # Override
    def _add(self, data, h):
        while self._get_at(h) != None:
            h += 1
            h %= self._get_length()
        self._array[h] = data

    # Override
    def lookup(self, data):
        h = self.hash(data)
        return self._lookup(data, h)
    
    # Internal
    # Override
    def _lookup(self, data, h):
        for other in self.iterate_data(h):
            if other == data:
                return True
            h += 1
            h %= self._get_length()
        return False
    
    # Override
    def iterate_data(self, h):
        while self._get_at(h) != None:
            yield self._get_at(h)
            h += 1
            h %= self._get_length()