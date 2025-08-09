from abc import ABC, abstractmethod

class IListNode(ABC):
    
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self):
        pass
    
    @abstractmethod
    def get_next(self):
        pass
    
    @abstractmethod
    def set_next(self, next):
        pass