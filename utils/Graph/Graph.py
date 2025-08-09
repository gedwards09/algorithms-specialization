from utils.Graph.EdgeImpFactory import EdgeImpFactory
from utils.Graph.GraphNode import GraphNode
from utils.Graph.IGraph import IGraph
from utils.Stack.LinkedListStack import LinkedListStack

class Graph(IGraph):

    def __init__(self, file, file_parse_mode="node", directed=False, header=False):
        # handler for directed versus undirected edges
        self._edge_imp = self.init_edge_imp(directed=directed)
        # index of nodes by name
        self._nodes = {}
        # index of edges by key
        self._edges = {}
        self.init_graph(file, file_parse_mode, header=header)
        # number of nodes
        self._n = len(list(self._nodes.keys()))
        # number of edges
        self._m = len(list(self._edges.keys()))

    def init_edge_imp(self, directed=False):
        if directed:
            return EdgeImpFactory.create(type=EdgeImpFactory.DirectedEdgeType)
        else:
            return EdgeImpFactory.create(type=EdgeImpFactory.UndirectedEdgeType)

    def init_graph(self, file, file_parse_mode, header=False):
        if file_parse_mode == "node":
            self.init_graph_node(file, header=header)
        elif file_parse_mode == "edge":
            self.init_graph_edges(file, header=header)

    def init_graph_node(self, file, header=False):
        max_vertex_num = 0
        for line in file:
            if header:
                header = False
                continue
            words = line.split()
            name = words[0]
            self.add_node(name)
            for word in words[1:]:
                self.parse_adjacent_node(name, word)
            max_vertex_num = max(int(name), max_vertex_num)
            for next_name in self._nodes[name].iterate_next():
                max_vertex_num = max(int(next_name), max_vertex_num)
        for i in range(1, max_vertex_num + 1):
            name = str(i)
            if name not in self._nodes:
                self.add_node(name)
    
    def add_node(self, name):
        self._nodes[name] = self.make_node(name)
        if hasattr(self, "_n"):
            self._n += 1

    def make_node(self, name):
        return GraphNode(name)
    
    def parse_adjacent_node(self, name, word):
        self.add_adjacent_nodes(name, word)
        self.add_to_edges(name, word)
    
    def add_adjacent_nodes(self, tail_name, head_name, weight_name=None):
        if weight_name != None:
            head_name += ',' + weight_name
        self._nodes[tail_name].add_next(head_name)

    def add_to_edges(self, tail_name, head_name, weight_name=None):
        key = self.get_key(tail_name, head_name, weight_name)
        if key not in self._edges:
            self._edges[key] = self.get_edge_tuple(tail_name, head_name, weight_name)
    
    def get_key(self, tail_name, head_name, weight_name=None):
        return self._edge_imp.get_key(tail_name, head_name, weight_name)
    
    def get_edge_tuple(self, tail_name, head_name, weight_name=None):
        return self._edge_imp.get_edge_tuple(tail_name, head_name, weight_name)
        
    def init_graph_edges(self, file, header=True):
        if not header:
            self.parse_headerless_edge_file(file)
            return
        for line in file:
            if header:
                header = False
                num_nodes = line.split()[0]
                self.init_graph_nodes(num_nodes)
                continue
            self.parse_edge(line)

    def parse_headerless_edge_file(self, file):
        file_arr = [line for line in file]
        num_nodes = self.get_max_vertex_number(file_arr)
        self.init_graph_nodes(num_nodes)
        for line in file_arr:
            self.parse_edge(line)

    def get_max_vertex_number(self, file_arr):
        return max([max([int(pc) for pc in line.split()]) for line in file_arr])

    def init_graph_nodes(self, num_nodes):
        for i in range(1,int(num_nodes)+1):
            name = str(i)
            self.add_node(name)

    def parse_edge(self, line):
        tail_name, head_name = line.split()
        self.add_edge(tail_name, head_name)

    def add_edge(self, tail_name, head_name, weight_name=None):
        self._edge_imp.add_edge(self, tail_name, head_name, weight_name)
        if hasattr(self, "_m"):
            self._m += 1

    def get_nodes(self):
        return self._nodes
    
    def get_node(self, node_name):
        return self._nodes[node_name]
    
    def get_node_count(self):
        return self._n
    
    def get_edges(self):
        return self._edges
    
    def get_edge(self, key):
        return self._edges[key]
    
    def get_edge_count(self):
        return self._m
    
    #
    # Iterates over graph nodes using Depth-First-Search (DFS) 
    # using optional node ordering if provided.
    # @param node_order   [in]  List of nodes to iterate over in order. 
    #                           If not specified, arbitrary ordering is used.
    # @param finish_order [out] Output array of nodes in finishing order.
    # @param node_counts  [out] Output array of the number of nodes traversed by each DFS call
    # @returns List of the sizes of each DFS call
    #
    def dfs_iterator(self, node_order = None, finish_order = None, node_counts = None):
        visited = {}
        if node_order != None:
            iterate_nodes = node_order
        else:
            iterate_nodes = self.get_nodes()
        for node_name in iterate_nodes:
            if int(node_name) not in visited:
                size = 0
                for node in self.dfs_from_node_iterator(int(node_name), visited, node_order, finish_order):
                    size += 1
                    yield node
                if node_counts != None:
                    node_counts.append(size)
 
    def dfs_from_node_iterator(self, start_num, visited, node_order, finish_order):
        stack = LinkedListStack()
        stack.push(start_num)
        while stack.get_size() > 0:
            current_num = stack.peek()
            if current_num in visited:
                if visited[current_num] != 1:
                    if finish_order != None:
                        finish_order.append(current_num)
                    visited[current_num] = 1
                _ = stack.pop()
                continue
            visited[current_num] = 0
            current = self.get_node(str(current_num))
            next_nums = [int(name) for name in current.iterate_next()]
            if node_order != None:
                next_nums.sort(key = lambda num: node_order.index(num) if num not in visited else 0, reverse=True)
            else:
                next_nums.sort(key = lambda num: 1 if num not in visited else 0, reverse=True)
            for num in next_nums:
                if num not in visited:
                    stack.push(num)
                else:
                    # have visited all remaining nodes
                    break
            yield current

    
    def dfs_set_iterator(self, node_order = None, finish_order = None):
        visited = {}
        if node_order != None:
            iterate_nodes = node_order
        else:
            iterate_nodes = self.get_nodes()
        for node_name in iterate_nodes:
            if int(node_name) not in visited:
                scc = {}
                for node in self.dfs_from_node_iterator(int(node_name), visited, node_order, finish_order):
                    scc[node.get_name()] = 1
                yield scc
    

    def to_string(self):
        return '\n'.join([node.to_string() for node in self._nodes.values()])