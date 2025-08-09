import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')
from TwoSatGraph import TwoSatGraph
from utils.List.ReversibleIndexedList import ReversibleIndexedList

def alg(filename):
    with open(filename, 'r') as file:
        graph = TwoSatGraph(file)
    return has_two_sat_solution(graph)

def has_two_sat_solution(graph):
    sizes = []
    for scc in graph.iterate_scc():
        for node_name in scc:
            neg_node_name = TwoSatGraph.get_neg_node_name(node_name)
            if neg_node_name in scc:
                return 0
    return 1

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./tsp-heuristic.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()

