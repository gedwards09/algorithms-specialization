from abc import abstractmethod
from utils.HashTable.IHashTable import IHashTable

class IArrayBackedHashTable(IHashTable):

    #
    # Iterates over hash table collisions starting at a given key
    #
    @abstractmethod
    def iterate_data(self, key):
        pass

    #
    # Hashing function
    #
    @abstractmethod
    def hash(self, key):
        pass

    # Internal
    @abstractmethod
    def _add(self, data, key):
        pass

    # Internal
    @abstractmethod
    def _lookup(self, data, key):
        pass
    
    # Protected
    @abstractmethod
    def _get_length(self):
        pass

    # Protected
    @abstractmethod
    def _get_at(self, i):
        pass
    
    # Protected
    @abstractmethod
    def _set_at(self, i, obj):
        pass
