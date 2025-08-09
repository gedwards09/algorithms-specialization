import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')

from utils.UnionFind.UnionFind import UnionFind

def alg(filename):
    skip_header = True
    set = UnionFind()
    with open(filename, 'r') as f:
        for line in f:
            if skip_header:
                skip_header = False
                _, m = line.split()
                m = int(m)
                continue
            set.append(int(''.join(line.split()), base=2))
    return get_max_3_sep_clusters(set, n_bits=m)

def get_max_3_sep_clusters(set, n_bits):
    m = n_bits
    dic = {}
    for binval in set:
        dic[binval] = binval
        i_mask = 0b01
        for i in range(m):
            add_1_sep_nodes(dic, binval, set, i_mask)
            i_mask <<= 1
    return set.get_cluster_count()

def add_1_sep_nodes(dic, binval, set, i_mask):
    trunc = binval | i_mask
    dic = key_value_union(dic, trunc, binval, set)
    trunc = binval & ~ i_mask
    dic = key_value_union(dic, trunc, binval, set)
    return dic

def key_value_union(dic, key, binval, set):
    if key in dic:
        set.union(dic[key], binval)
    else:
        dic[key] = binval
    return dic

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./hamming.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()