from HuffmanTreeNode import HuffmanTreeNode
from utils.Comparator.KeyComparator import KeyComparator
from utils.Heap.MinHeap import MinHeap

class HuffmanCode:
    s_key = lambda node: node.get_data()

    def __init__(self, file):
        self._size, self._weights = self.init_weights(file)
        self._root = self.init_huffman_tree()

    def init_weights(self, file):
        weights = [int(line) for line in file]
        return weights[0], weights[1:]

    def init_huffman_tree(self):
        heap = self.init_heap()
        while heap.size() > 1:
            one = heap.remove()
            two = heap.remove()
            parent = self._merge_nodes(one, two)
            heap.add(parent)
        # final node is the root node
        return heap.remove()
    
    def init_heap(self):
        comparator = KeyComparator(key = HuffmanCode.s_key)
        heap = MinHeap(length=self._size, comparator=comparator)
        for weight in self._weights:
            node = HuffmanTreeNode(weight)
            heap.add(node)
        return heap

    # Private
    def _merge_nodes(self, one, two):
        if one.get_data() > two.get_data():
            return self._merge_nodes(two, one)
        parent_weight = one.get_data() + two.get_data()
        parent = HuffmanTreeNode(parent_weight)
        parent.set_left(one)
        parent.set_right(two)
        return parent
    
    def get_height(self):
        return self._root.get_height()
    
    def get_min_length(self):
        return self._root.get_min_length()



    

