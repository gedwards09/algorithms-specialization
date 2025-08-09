from utils.Graph.Graph import Graph

class DirectedGraph(Graph):

    def __init__(self, file, file_parse_mode="node", header=False):
        super().__init__(file, file_parse_mode, directed=True, header=header)
        self.update_nodes()
        
    def update_nodes(self):
        max = 1
        for node_name in self.get_nodes():
            max = self.max_name_number(node_name, max)
            node = self.get_node(node_name)
            for next_name in node.iterate_next():
                max = self.max_name_number(next_name, max)
        self.make_missing_nodes(max)
    
    def make_missing_nodes(self, max):
        for i in range(1, max + 1):
            name = str(i)
            self.add_node_if_not_found(name)

    def add_node_if_not_found(self, name):
        if name not in self.get_nodes():
            self.add_node(name)

    def max_name_number(self, name, current):
        return max(int(name), current)