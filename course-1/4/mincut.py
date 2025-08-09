import sys
from MinCutGraph import MinCutGraph

def alg(filename):
    with open(filename, "r") as f:
        g = MinCutGraph(f)
    return g.get_min_cuts(85)

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./mincut.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()