from abc import ABC, abstractmethod

class IGraph(ABC):

    @abstractmethod
    def get_nodes(self):
        pass
    
    @abstractmethod
    def get_node(self, node_name):
        pass
    
    @abstractmethod
    def get_node_count(self):
        pass
    
    @abstractmethod
    def get_edges(self):
        pass
    
    @abstractmethod
    def get_edge(self, key):
        pass
    
    @abstractmethod
    def get_edge_count(self):
        pass

    # @abstractmethod
    # def dfs_iter(self):
    #     pass
    
    @abstractmethod
    def to_string(self):
        pass