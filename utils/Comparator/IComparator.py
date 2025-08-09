from abc import ABC, abstractmethod

class IComparator(ABC):

    @abstractmethod
    def compare(self, one, two):
        pass