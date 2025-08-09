import sys
sys.path.append("C:/Users/grege/Python/algorithms-specialization/")
from utils.Graph.WeightedGraph import WeightedGraph

def alg(filename):
    with open(filename, "r") as f:
        g = WeightedGraph(f)
    comparator = g.dijkstra()
    return ','.join([str(comparator.get(el)) for el in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]])

def __main__():
    if len(sys.argv) != 2:
        print("usage:python3 ./dijksta.py filename")
        return
    print(alg(sys.argv[1]))

if __name__ == "__main__":
    __main__()