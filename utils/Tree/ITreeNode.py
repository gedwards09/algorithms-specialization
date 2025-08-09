from abc import ABC, abstractmethod

class ITreeNode(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_left(seft):
        pass

    @abstractmethod
    def get_right(self):
        pass

    @abstractmethod
    def set_left(self, node):
        pass
    
    @abstractmethod
    def set_right(self, node):
        pass