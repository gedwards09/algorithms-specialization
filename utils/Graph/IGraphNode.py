from abc import ABC, abstractmethod

class IGraphNode(ABC):

    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def add_next(self, next):
        pass
    
    @abstractmethod
    def iterate_next(self):
        pass

    @abstractmethod
    def to_string(self):
        pass