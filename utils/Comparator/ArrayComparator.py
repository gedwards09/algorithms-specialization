from utils.Array.IArray import IArray
from utils.Comparator.IComparator import IComparator

class ArrayComparator(IComparator,IArray):

    def __init__(self, array):
        self._size = len(array)
        self._array = array

    # Override
    def compare(self, one, two):
        one_finite = self.is_finite_value(one)
        two_finite = self.is_finite_value(two)
        if one_finite and two_finite:
            return self._array[one] - self._array[two]
        elif not one_finite and not two_finite:
            return 0
        elif not one_finite:
            return 1
        else:
            return -1
        
    def is_finite_value(self, i):
        return self.is_valid(i) and self._array[i] != None

    def is_valid(self, i):
        return 0 <= i and i < self._size
    
    # Override
    def get_length(self):
        return self._size
        
    def set_array(self, array):
        self._size = len(array)
        self._array = array

    # Override
    def get(self, i):
        if self.is_valid(i):
            return self._array[i]
        
    # Override
    def set(self, i, data):
        if self.is_valid(i):
            self._array[i] = data