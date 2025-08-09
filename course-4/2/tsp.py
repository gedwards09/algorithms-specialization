import sys
import numpy as np

def alg(filename):
    with open(filename, "r") as f:
        n, arr = read_coordinates(f)
    return tsp(n, arr)

def read_coordinates(file):
    arr = [int(line) if len(line.split()) == 1 else [float(pc) for pc in line.split()] for line in file]
    return arr[0], arr[1:]

def tsp(n, ls):
    distances = init_distances(n, ls)
    # subset_key = binary indicator of whether binary digit i is included in subset 
    # for j present in subset_key
    #   dp_memo[subset_key][j] = shortest path visiting all verticies with start = 0 and end = j 
    dp_memo = {}
    one = 0b1
    dp_memo[one] = {0: 0}
    # iterate over increasing subset size. max subset size is n
    for _ in range(2, n+1):
        index = one
        new_memo = {}
        for subset_key in dp_memo:
            for j in range(1, n):
                if (one << j) & subset_key != 0:
                    continue
                new_key = (one << j) | subset_key
                if new_key not in new_memo:
                    new_memo[new_key] = {}
                new_memo[new_key][j] = get_min_tsp_dp_len(dp_memo, subset_key, j, n, distances)
            dp_memo[subset_key] = None
        dp_memo = new_memo
    max_subset_key = ~((~0b1) << (n-1))
    min_dist = None
    for idx in dp_memo[max_subset_key]:
        cur_dist = dp_memo[max_subset_key][idx] + distances[(idx, 0)]
        if min_dist == None or cur_dist <= min_dist:
            min_dist = cur_dist
    return int(min_dist)

# returns the solution from dp subproblems where
# dp_memo[subset_key][j] = minimum over k of dp_memo[subset minus {j}][k] + dist(k, j)
def get_min_tsp_dp_len(dp_memo, subset_key, j, n, distances):
    # i = 0 is finite if and only if subset = {1}
    # otherwise we start at index i = 1
    if subset_key == 0b1:
        return distances[(0,j)]
    min_dist = None
    for i in dp_memo[subset_key]:
        cur_dist = dp_memo[subset_key][i] + distances[(i,j)]
        if min_dist == None or cur_dist < min_dist:
            min_dist = cur_dist
    return min_dist

def init_distances(n, ls):
    distances = {}
    for i in range(n-1):
        distances[(i,i)] = 0.0
        for j in range(i+1, n):
            dist = np.sqrt((ls[i][0] - ls[j][0])**2 + (ls[i][1] - ls[j][1])**2)
            distances[(i,j)] = dist
            distances[(j,i)] = dist
    return distances

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./tsp.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()