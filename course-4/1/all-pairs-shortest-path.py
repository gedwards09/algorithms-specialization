import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')
from utils.Graph.WeightedGraph import WeightedGraph

def alg(filename):
    with open(filename, 'r') as f:
        g = WeightedGraph(file=f, file_parse_mode="edge", directed=True, header=True)
    return all_pairs_shortest_path_fast(g)

def all_pairs_shortest_path_fast(graph: WeightedGraph):
    # add edge "0" with distance 0 to each vertex
    # run bellman-ford to compute potential to change edge distances
    # run dijkstra for each node in graph to get the shorted weighted path for all pairs
    graph.add_fake_node()
    potential_array = graph.bellman_ford(start_num = 0)
    if potential_array == None:
        return "NULL"
    # print(potential_array._array)
    min_dist = None
    for start_num in range(1, graph.get_node_count()):
        comparator = graph.dijkstra(start_num=start_num, potential=potential_array)
        # print(start_num, comparator._array)
        for i in range(1, graph.get_node_count()):
            cur = comparator.get(i)
            if cur != None:
                cur -= potential_array.get(start_num)
                cur += potential_array.get(i)
                if min_dist == None or min_dist > cur:
                    min_dist = cur
    return min_dist

def all_pairs_shortest_path(graph):
    min_dist = None
    for start_num in range(1, graph.get_node_count()+1):
        comparator = graph.bellman_ford(start_num)
        if comparator == None:
            return "NULL"
        for i in range(1, graph.get_node_count()+1):
            cur = comparator.get(i)
            if cur != None:
                if min_dist == None or min_dist > cur:
                    min_dist = cur
    return min_dist

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./all-pairs-shortest-path.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()