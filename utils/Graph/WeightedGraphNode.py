from utils.Graph.GraphNode import GraphNode

class WeightedGraphNode(GraphNode):

    # Override
    def init_next(self, words):
        dict = {}
        for target in words[1:]:
            self.add_next(target)
        return dict
    
    # Override
    def add_next(self, target):
        key, value = target.split(',')
        if key not in self._next:
            self._next[key] = int(value)
        elif int(value) < self._next[key]:
            self._next[key] = int(value)
    
    def get_weight(self, name):
        if name not in self._next:
            return None
        return self._next[name]
    
    def set_weight(self, name, weight):
        self._next[name] = weight