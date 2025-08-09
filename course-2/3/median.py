import sys
sys.path.append("C:/Users/grege/Python/algorithms-specialization/")

from utils.Comparator.KeyComparator import KeyComparator
from utils.Heap.MinHeap import MinHeap

def alg(filename):
    arr = []
    with open(filename, "r") as f:
        return median([int(line) for line in f])
    
def median(arr):
    greater_comparator = KeyComparator(key = lambda val: val)
    greater_heap = MinHeap(comparator = greater_comparator)
    lesser_comparator = KeyComparator(key = lambda val: -val)
    lesser_heap = MinHeap(comparator = lesser_comparator)
    current = arr[0]
    output = current
    for i in range(1, len(arr)):
        el = arr[i]
        if el < current:
            lesser_heap.add(el)
        else:
            greater_heap.add(el)
        current = balance(current, lesser_heap, greater_heap)
        output += current
        output %= 10000
    return output

def balance(current, lesser_heap, greater_heap):
    while greater_heap.size() > lesser_heap.size() + 1:
        lesser_heap.add(current)
        current = greater_heap.remove()
    while greater_heap.size() < lesser_heap.size():
        greater_heap.add(current)
        current = lesser_heap.remove()
    return current

def __main__(arr):
    if len(sys.argv) != 2:
        print("usage:python3 ./median.py filename")
        return
    print(alg(sys.argv[1]))

if __name__ == "__main__":
    __main__()