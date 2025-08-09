import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')

from utils.Graph.IGraph import IGraph
from utils.UnionFind.UnionFind import UnionFind
from utils.Graph.WeightedGraph import WeightedGraph

def alg(filename):
    with open(filename, 'r') as file:
        g = WeightedGraph(file, file_parse_mode="edge", header=True)
    return kruskal(g, n_clusters=4)

def kruskal(graph: IGraph, n_clusters):
    node_set = UnionFind()
    for node_name in graph.get_nodes().keys():
        node_set.append(node_name)
    edges = [edge for edge in graph.get_edges().values()]
    edges.sort(key = lambda edge_triple: int(edge_triple[2]))
    cluster_count = graph.get_node_count()
    for edge in edges:
        first, second, weight = edge
        if node_set.find(first) == node_set.find(second):
            continue
        elif cluster_count == n_clusters:
            break
        node_set.union(first, second)
        cluster_count -= 1
    # final weight is the max separation distance of clusters
    return weight

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./clustering.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()