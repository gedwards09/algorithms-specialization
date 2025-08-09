from abc import ABC, abstractmethod

class IHeap(ABC):

    @abstractmethod
    def add(self, data):
        pass

    @abstractmethod
    def remove(self):
        pass
    
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def clear(self):
        pass