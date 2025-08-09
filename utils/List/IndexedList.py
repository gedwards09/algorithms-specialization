from utils.List.ArrayList import ArrayList

class IndexedList(ArrayList):

    def __init__(self, size):
        super().__init__(size)
        self._index = {}

    def append(self, data):
        super().append(data)
        self._index[data] = self.get_length() - 1
    
    def index(self, data):
        if data not in self._index:
            raise Exception("IndexedList.py:index: data element " + str(data) + " not found in index.")
        return self._index[data]
    
    # Override
    def set(self, i, data):
        old = self.get(i)
        if data != old:
            del self._index[old]
        super().set(i, data)
        self._index[data] = i
    
    # Override
    def swap(self, i, j):
        super().swap(i, j)
        self._index[self.get(i)] = i
        self._index[self.get(j)] = j
        