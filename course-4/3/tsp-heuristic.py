import sys
import numpy as np

def alg(filename):
    with open(filename, 'r') as f:
        n, points = read_tsp_file(f)
    return tsp_heuristic(n, points)

def read_tsp_file(file):
    arr = [int(line)\
            if len(line.split()) == 1\
            else [float(pc) for pc in line.split()[1:]]\
            for line in file]
    return arr[0], arr[1:]

def tsp_heuristic(n, points):
    first = points.pop(0)
    n -= 1
    dist = 0
    dest = first
    while n > 0:
        delta, dest, points = get_next_dest(dest, points)
        dist += delta
        n -= 1
    dist += np.sqrt((first[0] - dest[0])**2 + (first[1] - dest[1])**2)
    return int(dist)

def get_next_dest(cur_loc, points):
    min_dist_sq = None
    min_idx = -1
    for idx in range(len(points)):
        point = points[idx]
        cur_dist_sq = (point[0] - cur_loc[0])**2 + (point[1] - cur_loc[1])**2
        if min_dist_sq == None or cur_dist_sq < min_dist_sq:
            min_dist_sq = cur_dist_sq
            min_idx = idx
    destination = points.pop(min_idx)
    dist = np.sqrt(min_dist_sq)
    return dist, destination, points

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./tsp-heuristic.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()