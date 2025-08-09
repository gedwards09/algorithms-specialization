import random
import sys
sys.path.append("C:/Users/grege/Python/algorithms-specialization/")
from utils.Graph.Graph import Graph

random.seed(999)

class MinCutGraph(Graph):

    def __init__(self, file):
        super().__init__(file)
        # list of the edge keys of the graph
        self._edge_keys = list(self.get_edges())
    
    def get_min_cuts(self, times = 15):
        n_nodes = self.get_node_count()
        min = n_nodes * (n_nodes + 1) // 2
        for _ in range(times):
            curmin = self.randomized_min_cut()
            if curmin < min:
                min = curmin
        return min

    def randomized_min_cut(self):
        node_parent_map = self.init_node_parent_map()
        excluded_edges = {}
        for _ in range(self.get_node_count() - 2):
            edge = self.select_edge(node_parent_map, excluded_edges)
            parent_name, child_name = edge
            if parent_name > child_name:
                parent_name, child_name = child_name, parent_name
            parent_name = self.get_root_name(parent_name, node_parent_map)
            child_name = self.get_root_name(child_name, node_parent_map)
            node_parent_map[child_name] = parent_name
        return self.count_cuts(node_parent_map, excluded_edges)
    
    def init_node_parent_map(self):
        return {name: name for name in self.get_nodes().keys()}
    
    def select_edge(self, node_parent_map, excluded_edges):
        cur_edge_key = None
        while not self.is_valid(cur_edge_key, node_parent_map, excluded_edges):
            i = random.randint(0, self.get_edge_count() - 1)
            cur_edge_key = self._edge_keys[i]
        return self.get_edge(cur_edge_key)

    def is_valid(self, edge_key, node_parent_map, excluded_edges):
        if edge_key == None:
            return False
        elif edge_key in excluded_edges:
            return False
        node_name_1, node_name_2 = self.get_edge(edge_key)
        if self.get_root_name(node_name_1, node_parent_map) == self.get_root_name(node_name_2, node_parent_map):
            excluded_edges[edge_key] = 1
            return False
        return True
    
    def get_root_name(self, node_name, node_parent_map):
        next_name = node_parent_map[node_name]
        while next_name != node_name:
            node_name = next_name
            next_name = node_parent_map[node_name]
        return node_name
    
    def count_cuts(self, node_parent_map, excluded_edges):
        count = 0
        for key in self.get_edges():
            if self.is_valid(key, node_parent_map, excluded_edges):
                count += 1
        return count