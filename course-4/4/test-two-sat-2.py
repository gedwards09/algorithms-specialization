import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')
from TwoSatGraph import TwoSatGraph
from utils.List.ReversibleIndexedList import ReversibleIndexedList

def alg(filename):
    with open(filename, 'r') as file:
        graph = TwoSatGraph(file)
    print_graph(graph)
    return has_two_sat_solution(graph)


def has_two_sat_solution(g: TwoSatGraph):
    n = g.get_node_count()
    out = True
    # initialize empty list of size n
    finish_order = ReversibleIndexedList(n)
    for node in g.dfs_iterator(finish_order = finish_order):
        continue
    g.reverse_nodes()
    print(finish_order._array)
    finish_order.reverse()
    for scc in g.dfs_set_iterator(node_order = finish_order):
        ls = list(scc.keys())
        ls.sort()
        print(ls)
        for node_name in scc:
            neg_node_name = TwoSatGraph.get_neg_node_name(node_name)
            if out and neg_node_name in scc:
                print(node_name, neg_node_name)
                out = False
    return out

def print_graph(graph):
    arr = []
    for node_name in graph.get_nodes():
        node = graph.get_node(node_name)
        arr += [node_name + ' ' + next_name for next_name in node.iterate_next()]
    print('\n'.join(arr))

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./tsp-heuristic.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()

