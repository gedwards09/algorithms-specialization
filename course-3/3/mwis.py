import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')

# 
configuration = [1, 2, 3, 4, 17, 117, 517, 997]

def alg(filename):
    with open(filename, 'r') as file:
        weights = init_weights(file)
    mwis_sums = mwis(weights)
    return mwis_bitmap(weights, mwis_sums)

def init_weights(file):
    return [int(line) for line in file]

# 
# Determines the indices which make up the maximum weighted independent set (MWIS)
# param weights: weights[0] = # of elements
#                weights[i] = weight of the i-th element for each i > 0
# returns dictionary of the the indices of the maximum weighted independent set
#
def mwis(weights):
    max_weight_sums = [0 for _ in range(len(weights))]
    indices = {}
    for i in range(1, len(weights)):
        weight = weights[i]
        if i == 1:
            max_weight_sums[i] = weight
        elif max_weight_sums[i-1] > max_weight_sums[i-2] + weight:
            max_weight_sums[i] = max_weight_sums[i-1]
        else:
            max_weight_sums[i] = max_weight_sums[i-2] + weight
    return max_weight_sums

def mwis_bitmap(weights, mwis_sums):
    bitmasks = init_bitmasks()
    rc = 0
    idx = len(weights) - 1
    while idx > 0:
        if idx == 1 or mwis_sums[idx-2] + weights[idx] > mwis_sums[idx-1]:
            if idx in bitmasks:
                rc |= bitmasks[idx]
            idx -= 2
        else:
            idx -= 1
    return get_bin_string(rc)

def init_bitmasks():
    return {configuration[i] : 0b1 << (len(configuration) - i - 1) for i in range(len(configuration))}

def get_bin_string(rc):
    str = '00000000' + bin(rc)[2:]
    return str[-8:]

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./mwis.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()