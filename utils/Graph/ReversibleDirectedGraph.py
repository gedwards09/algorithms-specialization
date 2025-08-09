from utils.Graph.DirectedGraph import DirectedGraph
from utils.List.ReversibleIndexedList import ReversibleIndexedList
from utils.Graph.ReversibleGraphNode import ReversibleGraphNode

class ReversibleDirectedGraph(DirectedGraph):

    def __init__(self, file, file_parse_mode="edge", header=False):
        super().__init__(file, file_parse_mode=file_parse_mode, header=header)
        self.update_nodes()
        self.update_node_parents()

    # Override
    def make_node(self, line):
        return ReversibleGraphNode(line)
    
    def update_node_parents(self):
        for node in self.get_nodes().values():
            for next_name in node.iterate_next():
                next = self.get_node(next_name)
                next.add_parent(node.get_name())

    def reverse_nodes(self):
        for node in self.get_nodes().values():
            node.reverse()
    
    #
    # Returns sizes of the strongly connected components of the graph
    #
    def get_scc_sizes(self):
        finish_order = self.get_dfs_finish_order()
        finish_order.reverse()
        self.reverse_nodes()
        sizes = []
        for node in self.dfs_iterator(node_order = finish_order, node_counts = sizes):
            continue
        return sizes

    def get_dfs_finish_order(self):
        n = self.get_node_count()
        # initialize empty list of size n
        finish_order = ReversibleIndexedList(n)
        for node in self.dfs_iterator(finish_order = finish_order):
            continue
        return finish_order

    #
    # Iterator returns pointer to dict containing nodes in a single
    # strongly conencted component
    #
    def iterate_scc(self):
        finish_order = self.get_dfs_finish_order()
        finish_order.reverse()
        self.reverse_nodes()
        for scc_set in self.dfs_set_iterator(node_order = finish_order):
            yield scc_set
            