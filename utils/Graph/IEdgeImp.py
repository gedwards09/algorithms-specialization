from abc import ABC, abstractmethod

class IEdgeImp(ABC):

    @abstractmethod
    def get_key(self, tail_name, head_name, weight):
        pass

    @abstractmethod
    def get_edge_tuple(self, tail_name, head_name, weight):
        pass

    @abstractmethod
    def add_edge(self, graph, tail_name, head_name, weight):
        pass