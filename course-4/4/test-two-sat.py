import sys
from TwoSatGraph import TwoSatGraph

def alg(filename):
    with open(filename, 'r') as file:
        graph = TwoSatGraph(file)
    print_graph(graph)
    return ''
    #graph.reverse_nodes()
    node_num = -151
    finish_order = []
    visited = {}
    for node in graph.dfs_from_node_iterator(node_num, visited = visited, node_order=None, finish_order=finish_order):
        continue
    print(finish_order)
    print(finish_order.index(node_num), finish_order.index(-node_num))
    return -node_num in visited

def print_graph(graph):
    arr = []
    for node_name in graph.get_nodes():
        node = graph.get_node(node_name)
        arr += [transform_node_name(graph, node_name) + ' ' + transform_node_name(graph, next_name) for next_name in node.iterate_next()]
    print('\n'.join(arr))

def transform_node_name(graph, node_name):
    if int(node_name) < 0:
        return str(graph.get_node_count() + int(node_name))
    return node_name

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./tsp-heuristic.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()