import sys
sys.path.append("C:/Users/grege/Python/algorithms-specialization/")

import random
random.seed(999)

from utils.Comparator.KeyComparator import KeyComparator
from utils.Heap.MinHeap import MinHeap

def __main__():
    key = lambda one: str(one)
    for n in range(10):
        length = 2 ** n
        run_tests(length)
        run_tests(length, key)

def run_tests(max, key = None):
    arr = [i for i in range(max)]
    arr = permute(arr)
    comparator = KeyComparator(key = key)
    heap = MinHeap(comparator = comparator)
    for el in arr:
        heap.add(el)
    arr.sort(key = key)
    i = 0
    while not heap.is_empty():
        assert heap.remove() == arr[i]
        i += 1

def permute(arr):
    n = len(arr)
    for i in range(n):
        swap(arr, i, random.randint(i, n - 1))
    return arr

def swap(arr, i, j):
    if i != j:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

if __name__ == "__main__":
    __main__()