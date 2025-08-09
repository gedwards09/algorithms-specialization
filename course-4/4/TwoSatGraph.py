import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')
from utils.Graph.ReversibleDirectedGraph import ReversibleDirectedGraph

class TwoSatGraph(ReversibleDirectedGraph):

    def __init__(self, file):
        super().__init__(file, file_parse_mode = "edge", header=True)
    
    # Override
    def init_graph_nodes(self, num_nodes):
        for i in range(1,int(num_nodes)+1):
            name = str(i)
            self.add_node(name)
            neg_name = TwoSatGraph.get_neg_node_name(name)
            self.add_node(neg_name)
    
    def get_neg_node_name(node_name):
        return str(-int(node_name))

    # Override
    def parse_edge(self, line):
        one_num, two_num = [int(pc) for pc in line.split()]
        if one_num == two_num:
            self.add_edge(str(-one_num), str(one_num))
        elif one_num == -two_num:
            return # tautology
        else:
            self.add_edge(str(-one_num), str(two_num))
            self.add_edge(str(-two_num), str(one_num))
    
    # Override
    def make_missing_nodes(self, max):
        nodes = self.get_nodes()
        for i in range(1, max + 1):
            name = str(i)
            self.add_node_if_not_found(name)
            neg_name = str(-i)
            self.add_node_if_not_found(neg_name)

    # Override
    def max_name_number(self, name, current):
        return max(abs(int(name)), current)

