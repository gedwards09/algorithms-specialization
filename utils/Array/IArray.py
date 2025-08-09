from abc import ABC, abstractmethod

class IArray(ABC):

    @abstractmethod
    def get_length(self):
        pass

    @abstractmethod
    def get(self, i):
        pass
        
    @abstractmethod
    def set(self, i, data):
        pass