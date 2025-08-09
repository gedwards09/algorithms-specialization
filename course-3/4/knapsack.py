import sys
import time

def alg(filename):
    with open(filename, 'r') as f:
        size, n_items, items = read_weights(f)
    items.sort(key=lambda item: 1.0 * item['value']/item['weight'], reverse=True)
    return knapsack(size, n_items, items)

def read_weights(file):
    raw_items = [unpack(line) for line in file]
    size = raw_items[0]['value']
    n_items = raw_items[0]['weight']
    return size, n_items, raw_items[1:]

def unpack(line):
    val, weight = line.split(' ')
    return {'value': int(val), 'weight':int(weight)}

def knapsack(size, n_items, items):
    memo = [0 for _ in range(size+1)]
    start = time.time()
    for item_idx in range(n_items):
        item = items[item_idx]
        value = item['value']
        weight = item['weight']
        for j in range(size, 0, -1):
            memo[j] = max(memo[j], (value + memo[j-weight] if j >= weight else 0))
        if (item_idx + 1) % 500 == 0:
            print("\t batch: {0} complete {1}".format(item_idx + 1, (time.time() - start) // 1))
    return memo[-1]

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./knapsack.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()