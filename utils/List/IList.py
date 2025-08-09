from abc import ABC, abstractmethod

class IList(ABC):

    @abstractmethod
    def get_length(self):
        pass

    @abstractmethod
    def append(self):
        pass

    @abstractmethod
    def get(self, i):
        pass

    @abstractmethod
    def set(self, i, data):
        pass