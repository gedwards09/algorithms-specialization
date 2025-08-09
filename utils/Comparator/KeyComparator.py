from utils.Comparator.IComparator import IComparator

class KeyComparator(IComparator):

    def __init__(self, key = None):
        self._comparator = self.init_comparator(key)

    #
    # Use key to build comparator or use the default
    #
    def init_comparator(self, key):
        if key == None:
            return lambda one, two: 1 if one > two else -1 if one < two else 0
        return lambda one, two: 1 if key(one) > key(two) else -1 if key(one) < key(two) else 0
    
    # Override
    def compare(self, one, two):
        return self._comparator(one, two)