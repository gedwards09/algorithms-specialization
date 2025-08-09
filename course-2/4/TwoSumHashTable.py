from utils.HashTable.IArrayBackedHashTable import IArrayBackedHashTable
from utils.HashTable.IHashTable import IHashTable

class TwoSumHashTable(IHashTable):

    def __init__(self, table: IArrayBackedHashTable = None, target = 10_000):
        self._table = table
        self._target = target
        self._values = {}

    # Override
    def add(self, data):
        h = self.hash(data)
        self._table._add(data, h)

    # Override
    def lookup(self, data):
        h = self.hash(data)
        return self._table._lookup(data, h)

    #
    # Counts the number of values in range [-target, +target] (inclusive) which
    # have distinct table elements that sum to that value
    #
    def count_target_values(self, data):
        count = 0
        for i in range(-1, 2):
            k = self.hash(- data + i * self._target)
            for codata in self._table.iterate_data(k):
                if data == codata:
                    continue
                s = data + codata
                if -self._target <= s and s <= self._target and s not in self._values:
                    self._values[s] = ''
                    count += 1
        return count
    
    # Override
    def hash(self, key):
        key = self.prehash(key)
        return self._table.hash(key)

    def prehash(self, data):
        return data // self._target