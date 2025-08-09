from utils.Tree.TreeNode import TreeNode

class HuffmanTreeNode(TreeNode):
    # Override
    def __init__(self, data):
        self._parent = None
        self._height = 0
        self._min_length = 0
        super().__init__(data)

    def get_height(self):
        return self._height
    
    def get_min_length(self):
        return self._min_length

    # Override
    def set_left(self, node):
        super().set_left(node)
        self._set_parent_for_child(node)

    # Private
    def _set_parent_for_child(self, node):
        node._set_parent(self)
        self._update_height_for_child(node)
        self._update_min_length()
    
    # Private
    def _set_parent(self, node):
        self._parent = node

    # Private
    def _update_height_for_child(self, node):
        child_height = node.get_height()
        if child_height + 1 > self._height:
            self._height = child_height + 1

    # Private
    def _update_min_length(self):
        if self.get_left() == None or self.get_right() == None:
            return
        left_min_length = self.get_left().get_min_length()
        right_min_length = self.get_right().get_min_length()
        if left_min_length < right_min_length:
            self._min_length = left_min_length + 1
        else:
            self._min_length = right_min_length + 1
        
    # Override
    def set_right(self, node):
        super().set_right(node)
        self._set_parent_for_child(node)