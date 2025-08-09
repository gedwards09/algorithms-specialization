from utils.Graph.GraphNode import GraphNode

class ReversibleGraphNode(GraphNode):

    def __init__(self, line):
        super().__init__(line)
        self._reversed = False
        self._parents = []

    # Override
    def iterate_next(self):
        if self._reversed:
            for parent_name in self.iterate_parents():
                yield parent_name
        else:
            for node_name in super().iterate_next():
                yield node_name

    def add_parent(self, parent):
        self._parents.append(parent)

    def iterate_parents(self):
        for parent in self._parents:
            yield parent

    def reverse(self):
        self._reversed = not self._reversed
