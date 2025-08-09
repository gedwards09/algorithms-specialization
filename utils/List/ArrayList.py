from utils.List.IList import IList

class ArrayList(IList):

    def __init__(self, size = 10):
        self._array = [None for _ in range(size)]
        self._size = size
        self._length = 0

    def __iter__(self):
        for i in range(self._length):
            yield self._array[i]

    def get_length(self):
        return self._length

    def append(self, data):
        if self._length == self._size:
            self.resize()
        self._array[self._length] = data
        self._length += 1

    def resize(self):
        self._array = self._array + [0 for _ in range(self._size)]
        self._size *= 2

    def get(self, i):
        if not self.is_valid(i):
            raise Exception("ArrayList.py:get: access {0} out of range {1}".format(i, self._length))
        return self._array[i]
    
    def is_valid(self, i):
        return i >= 0 and i < self._length
    
    def set(self, i, data):
        if self.is_valid(i):
            self._array[i] = data
    
    def swap(self, i, j):
        if not self.is_valid(i) and self.is_valid(j):
            raise Exception()
        one = self._array[i]
        two = self._array[j]
        self._array[j] = one
        self._array[i] = two
        