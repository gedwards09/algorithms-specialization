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
    n = g.get_node_count()
    # initialize empty list of size n
    finish_order = ReversibleIndexedList(n)
    for node in g.dfs_iterator(finish_order = finish_order):
        continue
    g.reverse_nodes()
    finish_order.reverse()
    s = []
    for set in g.dfs_set_iterator(node_order = finish_order):
        ls = list(set.keys())
        print(ls)
        s.append(len(ls))
    s.sort(reverse = True)
    return ','.join([str(s[i]) if i < len(s) else '0' for i in range(times)])


def reverse_dfs(g: IGraph, node_order = None, start_order = None, finish_order = None):
    g.reverse_nodes()
    return g.dfs(node_order, start_order, finish_order)

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./scc.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()