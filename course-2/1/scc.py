import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')
from utils.List.ReversibleIndexedList import ReversibleIndexedList
from utils.Graph.IGraph import IGraph
from utils.Graph.ReversibleDirectedGraph import ReversibleDirectedGraph

def alg(filename):
    with open(filename, 'r') as f:
        g = ReversibleDirectedGraph(f, header=False)
    return get_connected_component_sizes(g)

def get_connected_component_sizes(g: IGraph, times = 5):
    sizes = g.get_scc_sizes()
    sizes.sort(reverse = True)
    return ','.join([str(sizes[i]) if i < len(sizes) else '0' for i in range(times)])

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./scc.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()