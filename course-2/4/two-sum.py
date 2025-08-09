import sys
sys.path.append("C:/Users/grege/Python/algorithms-specialization")

from ArrayBackedHashTableFactory import ArrayBackedHashTableFactory
from TwoSumHashTable import TwoSumHashTable

def alg(filename):
    with open(filename, 'r') as f:
        return two_sum([int(line) for line in f])
    
def two_sum(arr):
    arr.sort()
    factory = ArrayBackedHashTableFactory(num_elements = len(arr))
    # table = factory.create('Chained')
    table = factory.create('Sequential')
    hash = TwoSumHashTable(table = table, target = 10_000)
    for el in arr:
        hash.add(el)
    count = 0
    for el in arr:
        count += hash.count_target_values(el)
    return count

def __main__():
    if len(sys.argv) != 2:
        print("usage:python3 ./two-sum.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()