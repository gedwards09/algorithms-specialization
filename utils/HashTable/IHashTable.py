from abc import ABC, abstractmethod

class IHashTable(ABC):

    @abstractmethod
    def add(self, data):
        pass

    @abstractmethod
    def lookup(self, data):
        pass