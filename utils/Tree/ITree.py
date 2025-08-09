from abc import ABC, abstractmethod

class ITree(ABC):
    @abstractmethod
    def get_root(self):
        pass

    @abstractmethod
    def put(self, data):
        pass