from utils.Comparator.IComparator import IComparator
from utils.Heap.IHeap import IHeap

class MinHeap(IHeap):

    def __init__(self, length = 10, comparator: IComparator = None):
        self._array = [None for _ in range(length)]
        self._length = length
        self._size = 0
        self._comparator = comparator

    # Override
    def add(self, data):
        if self._size + 1 >= len(self._array):
            self._resize()
        self._array[self._size + 1] = data
        self._size += 1
        self.up_heapify()

    # Private
    def _resize(self):
        self._array = self._array + [None for _ in range(self._length)]
        self._length *= 2

    # Protected
    def up_heapify(self):
        self._up_heapify(self._size)

    # Protected
    def _up_heapify(self, index):
        while index > 1 and self.compare(self._array[index], self._array[index // 2]) < 0:
            self._swap(index, index // 2)
            index = index // 2

    def compare(self, one, two):
        return self._comparator.compare(one, two)

    # Protected
    def _swap(self, i, j):
        tmp = self._array[i]
        self._array[i] = self._array[j]
        self._array[j] = tmp

    # Override
    def remove(self):
        if self._size == 0:
            raise Exception("MaxHeap:remove: Attempt to remove item from empty Heap")
        data = self._array[1]
        self._array[1] = self._array[self._size]
        self._size -= 1
        self.down_heapify()
        return data
    
    # Protected
    def down_heapify(self):
        self._down_heapify(1)

    # Protected
    def _down_heapify(self, index):
        while index <= self._size // 2:
            max_child_index = 2 * index \
                if self.compare(self._array[2 * index], self._array[2 * index + 1]) < 0\
                else 2 * index + 1
            if self.compare(self._array[index], self._array[max_child_index]) > 0:
                self._swap(index, max_child_index)
                index = max_child_index
            else:
                break

    # Override
    def size(self):
        return self._size
    
    # Override
    def is_empty(self):
        return self._size == 0
    
    # Override
    def clear(self):
        self._size = 0

    def to_string(self):
        return ','.join([str(el) for el in self._array[1:self._size + 1]])

    # Protected
    def _get_at(self, i):
        return self._array[i]