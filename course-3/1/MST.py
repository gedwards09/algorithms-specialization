import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')

from utils.Comparator.ArrayComparator import ArrayComparator
from utils.Graph.IGraph import IGraph
from utils.Heap.RelaxableMinHeap import RelaxableMinHeap
from utils.Graph.WeightedGraph import WeightedGraph

def alg(filename):
    with open(filename, 'r') as file:
        g = WeightedGraph(file, file_parse_mode="edge", header=True)
    return MST_cost_prim(g)

def MST_cost_prim(g: IGraph, start_num = 1):
    visited = {}
    cost = 0
    comparator = init_comparator(g, start_num)
    heap = RelaxableMinHeap(comparator=comparator)
    heap.add(start_num)
    while heap.size() > 0:
        node_num = heap.remove()
        visited[node_num] = 1
        cost += comparator.get(node_num)
        node = g.get_node(str(node_num))
        for next_name in node.iterate_next():
            next_num = int(next_name)
            if next_num not in visited:
                weight = node.get_weight(next_name)
                current_weight = comparator.get(next_num)
                if current_weight == None or weight < int(comparator.get(next_num)):
                    comparator.set(next_num, weight)
                    heap.relax_or_add(next_num)
    return cost

def init_comparator(g: IGraph, start_num):
    distance = init_distance(g, start_num)
    return ArrayComparator(distance)

def init_distance(g: IGraph, start_num):
    return [0 if i == start_num else None for i in range(g.get_node_count() + 1)]

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./MST.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()