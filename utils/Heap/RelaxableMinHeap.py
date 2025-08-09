from utils.Comparator.IComparator import IComparator
from utils.Heap.MinHeap import MinHeap

class RelaxableMinHeap(MinHeap):

    def __init__(self, length = 10, comparator:IComparator = None):
        super().__init__(length, comparator)
        self._index = {}

    # Override
    def add(self, data):
        self._index[data] = self.size() + 1
        super().add(data)

    # Protected
    # Override
    def _swap(self, i, j):
        self._index[self._get_at(i)] = j
        self._index[self._get_at(j)] = i
        super()._swap(i, j)

    # Override
    def remove(self):
        data = super().remove()
        self._index[data] = None
        return data
    
    def relax(self, data):
        self._relax(self._index[data])
    
    def relax_or_add(self, data):
        if data in self._index and self._index[data] != None:
            self._relax(self._index[data])
        else:
            self.add(data)

    def _relax(self, index):
        self._up_heapify(index)
