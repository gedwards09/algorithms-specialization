from utils.Tree.ITreeNode import ITreeNode

class TreeNode(ITreeNode):
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
    
    # Override
    def get_data(self):
        return self._data

    # Override
    def get_left(self):
        return self._left

    # Override
    def get_right(self):
        return self._right

    # Override
    def set_left(self, node):
        self._left = node
    
    # Override
    def set_right(self, node):
        self._right = node
