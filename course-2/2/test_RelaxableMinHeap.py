import sys
sys.path.append("C:/Users/grege/Python/algorithms-specialization/")

import random
random.seed(999)

from utils.Comparator.ArrayComparator import ArrayComparator
from utils.Heap.RelaxableMinHeap import RelaxableMinHeap

def run_tests():
    run_test(5)

def run_test(length):
    distance = [i for i in range(length)]
    comparator = ArrayComparator(distance)
    heap = RelaxableMinHeap(comparator = comparator)
    add_to_heap(heap, length)
    read_heap(heap)
    relax(heap, distance, init_distance(length))
    read_heap(heap)
    relax(heap, distance, [0, 5, 1000, 10, 1001])
    read_heap(heap)
    relax(heap, distance, [0, 5, 7, 8, 14])
    read_heap(heap)
    relax(heap, distance, [1, 5, 2, 4, 3])
    read_heap(heap)
    relax(heap, distance, [5, 4, 3, 2, 1])
    read_heap(heap)
    empty_heap(heap)

def init_distance(length):
    return [0 if i == 0 else 1000 + i for i in range(length)]

def relax(heap, distance, new_distance):
    for i in range(len(distance)):
        distance[i] = new_distance[i]
        heap.relax(i)


def add_to_heap(heap, length):
    for i in range(length):
        heap.add(i)

def read_heap(heap):
    print('\t', heap.to_string())

def empty_heap(heap):
    s = ''
    while heap.size() > 0:
        data = heap.remove()
        s += str(data) + ','
    print(s[:-1])

def __main__():
    run_tests()

if __name__ == "__main__":
    __main__()