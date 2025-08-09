from utils.Factory.IFactory import IFactory
from utils.HashTable.IArrayBackedHashTable import IArrayBackedHashTable
from utils.HashTable.ChainedHashTable import ChainedHashTable
from utils.HashTable.SequentialAddressHashTable import SequentialAddressHashTable

class ArrayBackedHashTableFactory(IFactory):

    def __init__(self, num_elements = None):
        self._num_elements = num_elements

    def create(self, type) -> IArrayBackedHashTable:
        if type == 'Sequential':
            return SequentialAddressHashTable(self._num_elements)
        elif type == 'Chained':
            return ChainedHashTable(self._num_elements)
        else: # default
            return ChainedHashTable(self._num_elements)