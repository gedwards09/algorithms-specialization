from abc import abstractmethod
from math import sqrt, floor, log2
from utils.HashTable.IArrayBackedHashTable import IArrayBackedHashTable

#
# Abstract implementation for an array backed hash table
#
class ArrayBackedHashTable(IArrayBackedHashTable):
    # default length
    s_default_length = 2 ** 20
    # multiplicative constant for hash function
    s_mult_const = (sqrt(5) - 1) / 2
    # length scale factor
    s_scale_factor = sqrt(5)

    def __init__(self, num_elements = None):
        # length oof the backing array
        self._length = self.init_length(num_elements)
        # backing array
        self._array = self.init_array()
        # size of the hash table
        self._size = 0

    def init_array(self):
        return [None for _ in range(self._length)]

    def init_length(self, num_elements):
        if num_elements == None:
            return self.get_default_length()
        length = min(self.get_scale_factor() * num_elements, self.get_default_length())
        return 2 ** floor(log2(length))
    
    def get_default_length(self):
        return ArrayBackedHashTable.s_default_length
    
    def get_mult_const(self):
        return ArrayBackedHashTable.s_mult_const

    def get_scale_factor(self):
        return ArrayBackedHashTable.s_scale_factor

    def hash(self, key):
        return floor(self._get_length() * (key * self.get_mult_const() % 1))

    # Protected
    # Override
    def _get_length(self):
        return self._length

    # Protected
    # Override
    def _get_at(self, i):
        return self._array[i]
    
    # Protected
    # Override
    def _set_at(self, i, obj):
        self._array[i] = obj

    # Protected
    def _increment_size(self):
        self._size += 1
        if self._size > self._length / self.get_mult_const():
            self._resize_array()

    # Private
    def _resize_array(self):
        raise Exception("Not Implemented")
