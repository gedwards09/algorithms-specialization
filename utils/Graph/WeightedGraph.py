from utils.Array.IArray import IArray
from utils.Comparator.ArrayComparator import ArrayComparator
from utils.Graph.Graph import Graph
from utils.Graph.WeightedGraphNode import WeightedGraphNode
from utils.Heap.RelaxableMinHeap import RelaxableMinHeap


class WeightedGraph(Graph):

    # Override
    def make_node(self, name):
        return WeightedGraphNode(name)
    
    # Override
    def parse_adjacent_node(self, tail_name, word):
        head_name, weight_name = word.split(',')
        self.add_adjacent_nodes(tail_name, head_name, weight_name)
        self.add_to_edges(tail_name, head_name, weight_name)
        
    # Override
    def parse_edge(self, line):
        tail_name, head_name, weight_name = line.split()
        self.add_edge(tail_name, head_name, weight_name)
    
    ##
    # Run dijkstra's algorithm from the specified starting node
    ##
    def dijkstra(self, start_num = 1, potential: IArray = None):
        visited = {}
        comparator = self._init_dijkstra_comparator(start_num)
        heap = self._init_dijkstra_heap(comparator)
        heap.add(start_num)
        while heap.size() > 0:
            current_num = heap.remove()
            visited[current_num] = 1
            current = self.get_node(str(current_num))
            for next in current.iterate_next():
                next_num = int(next)
                if next_num not in visited:
                    weight = current.get_weight(next)
                    if potential != None: 
                        weight += potential.get(current_num)
                        weight -= potential.get(next_num)
                    if weight < 0:
                        # return none if any edge weight is negative
                        raise Exception("WeightedGraph.py:dijkstra:negative weight edge detected")
                    if self._relax_dijkstra_comparator(comparator, current_num, next_num, weight):
                        heap.relax_or_add(next_num)
        return comparator

    # Private
    def _init_dijkstra_comparator(self, start_num):
        distance = self._init_dijkstra_distance(start_num)
        return ArrayComparator(distance)

    # Private
    def _init_dijkstra_heap(self, comparator):
        return RelaxableMinHeap(comparator = comparator)

    # Private
    def _init_dijkstra_distance(self, start_num):
        return [0 if i == start_num else None for i in range(self.get_node_count() + 1)]
    
    # Private
    def _relax_dijkstra_comparator(self, comparator, current_num, next_num, weight):
        if comparator.get(current_num) != None and \
            (comparator.get(next_num) == None or comparator.get(next_num) > comparator.get(current_num) + weight):
            data = comparator.get(current_num) + weight
            comparator.set(next_num, data)
            return True
        return False
    
    ##
    # Run Bellman-Ford algorithm from the specified starting node
    ##
    def bellman_ford(self, start_num = 1):
        comparator = self._init_dijkstra_comparator(start_num)
        for _ in range(self.get_node_count()):
            for edge in self.get_edges().values():
                tail, head, weight = WeightedGraph.unpack_edge_int(edge)
                self._relax_dijkstra_comparator(comparator, tail, head, weight)
        for edge in self.get_edges().values():
            tail, head, weight = WeightedGraph.unpack_edge_int(edge)
            head_dist = comparator.get(head)
            tail_dist = comparator.get(tail)
            if head_dist != None and tail_dist != None:
                if comparator.get(head) > comparator.get(tail) + weight:
                    return None
        return comparator 

    def unpack_edge_int(edge):
        return [int(el) for el in edge]
    
    ##
    # Adds a fake node connected to all other nodes by edge of distance zero
    # Uses default fake node name if none passes
    ##
    def add_fake_node(self, fake_node_num=0):
        fake_node_name = str(fake_node_num)
        if fake_node_name in self.get_nodes():
            raise Exception("WeightedGraph.py:add_fake_node:Node with specified number already exists")
        self.add_node(fake_node_name)
        for node_name in self.get_nodes():
            if node_name == fake_node_name:
                continue
            self.add_edge(fake_node_name, node_name, "0")
