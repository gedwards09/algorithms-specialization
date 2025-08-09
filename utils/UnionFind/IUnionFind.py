from abc import ABC, abstractmethod

class IUnionFind(ABC):

    @abstractmethod
    def find(self, data):
        pass

    @abstractmethod
    def union(self, one, two):
        pass