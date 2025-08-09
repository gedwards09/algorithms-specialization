from utils.UnionFind.IUnionFind import IUnionFind

class UnionFind(IUnionFind):
    def __init__(self):
        self._size = 0
        # array of data elements
        self._data = []
        # stores the index of each data element in the backing array
        self._index = {}
        # stores the index of the parent of each data alement
        self._parent_index = []
        # stored the rank of each data element
        self._rank = []
        # stores the number of distinct clusters
        self._cluster_count = 0

    def get_rank(self, data):
        index = self._index[data]
        return self._rank[index]
    
    def get_cluster_count(self):
        return self._cluster_count
    
    def __iter__(self):
        for key in self._index.keys():
            yield key
    
    def append(self, data):
        # its already in the set
        if data in self._index:
            return
        self._data.append(data)
        data_index = self._size
        self._index[data] = data_index
        self._parent_index.append(data_index)
        self._rank.append(0)
        self._size += 1
        self._cluster_count += 1
        
    # Override
    def union(self, one, two):
        one_root_idx = self._find_root_idx(one)
        two_root_idx = self._find_root_idx(two)
        self._union_root_idxs(one_root_idx, two_root_idx)

    # Private
    def _union_root_idxs(self, one_idx, two_idx):
        if one_idx == two_idx:
            return
        self._cluster_count -= 1
        one_rank = self._rank[one_idx]
        two_rank = self._rank[two_idx]
        if one_rank > two_rank:
            self._parent_index[two_idx] = one_idx
        elif one_rank < two_rank:
            self._parent_index[one_idx] = two_idx
        else: # equality
            self._rank[one_idx] += 1
            self._parent_index[two_idx] = one_idx 
        
    # Override
    def find(self, data):
        if data not in self._index:
            raise Exception("UnionFind: Data element not found")
        parent_idx = self._find_root_idx(data)
        return self._data[parent_idx]
    
    # Private
    def _find_root_idx(self, data):
        current_idx = self._index[data]
        parent_idx = self._parent_index[current_idx]
        while parent_idx != current_idx:
            current_idx = parent_idx
            parent_idx = self._parent_index[current_idx]
        self._compress_path(data, parent_idx)
        return parent_idx

    # Private
    def _compress_path(self, data, root_idx):
        current_idx = self._index[data]
        while current_idx != root_idx:
            tmp = self._parent_index[current_idx]
            self._parent_index[current_idx] = root_idx
            current_idx = tmp