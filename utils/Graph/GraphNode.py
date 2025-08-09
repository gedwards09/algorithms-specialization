from utils.Graph.IGraphNode import IGraphNode

class GraphNode(IGraphNode):

    def __init__(self, line):
        node_names = line.split()
        self._name = self.init_name(node_names)
        self._next = self.init_next(node_names)

    def init_name(self, node_names):
        return node_names[0]
    
    def init_next(self, node_names):
        return node_names[1:]

    def get_name(self):
        return self._name
    
    def add_next(self, next):
        self._next.append(next)
    
    def iterate_next(self):
        for name in self._next:
            yield str(name)

    def get_next_count(self):
        return len(self._next)

    def to_string(self):
        return self._name + ': ' + ' '.join([name for name in self._next])
    
