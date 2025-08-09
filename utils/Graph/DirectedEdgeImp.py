from utils.Graph.IEdgeImp import IEdgeImp

class DirectedEdgeImp(IEdgeImp):

    # Override
    def get_key(self, tail_name, head_name, weight_name=None):
        if weight_name != None:
            return str(hash(tail_name)) + '|' + str(hash(head_name)) + '|' + str(hash(weight_name))
        else:
            return str(hash(tail_name)) + '|' + str(hash(head_name))

    # Override
    def get_edge_tuple(self, tail_name, head_name, weight_name=None):
        if weight_name != None:
            return (tail_name, head_name, weight_name)
        else:
            return (tail_name, head_name)
    
    # Override
    def add_edge(self, graph, tail_name, head_name,weight_name=None):
        graph.add_adjacent_nodes(tail_name, head_name, weight_name)
        graph.add_to_edges(tail_name, head_name, weight_name)