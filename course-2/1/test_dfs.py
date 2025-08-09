import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')
from utils.Graph.Graph import Graph

def alg(filename):
    with open(filename, 'r') as f:
        g = Graph(f)
    print(g.to_string())
    node_order = [int(name) for name in g.get_nodes().keys()]
    node_order.sort()
    for node in g.dfs_iterator(node_order=node_order):
        print(node.get_name())

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./test-dfs.py filename")
        return
    filename = sys.argv[1]
    alg(filename)

if __name__ == "__main__":
    __main__()