from abc import ABC, abstractmethod

class IStack(ABC):

    @abstractmethod
    def get_head(self):
        pass
    
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def has_next(self):
        pass