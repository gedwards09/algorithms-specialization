from utils.Graph.IEdgeImp import IEdgeImp

class UndirectedEdgeImp(IEdgeImp):

    # Override
    def get_key(self, tail_name, head_name, weight_name=None):
        out = hash(tail_name) ^ hash(head_name)
        if weight_name != None:
            out ^= hash(weight_name)
        return out

    # Override
    def get_edge_tuple(self, tail_name, head_name, weight_name=None):
        if head_name < tail_name:
            return self.get_edge_tuple(head_name, tail_name, weight_name)
        elif weight_name != None:
            return (head_name, tail_name, weight_name)
        else:
            return (head_name, tail_name)
        
    # Override
    def add_edge(self, graph, tail_name, head_name, weight_name=None):
        graph.add_adjacent_nodes(tail_name, head_name, weight_name)
        graph.add_adjacent_nodes(head_name, tail_name, weight_name)
        graph.add_to_edges(tail_name, head_name, weight_name)