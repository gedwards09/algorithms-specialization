import sys
import math

def alg(filename):
    arr = init_arr(filename)
    return get_second_max(arr, False)

def init_arr(filename):
    with open(filename, 'r') as f:
        input = f.readline().split(' ')
    two_power = 1
    while two_power < len(input):
        two_power *= 2
    return [int(input[i]) if i < len(input) else 0 for i in range(two_power)]

def get_second_max(arr, verbose):
    max, sec, comps = r_get_second_max(arr)
    if verbose:
        n = len(arr)
        expected = n + math.log2(n) - 2
        print("{0} comparisons. Expected {1}".format(comps, expected))
    return arr[sec]

def r_get_second_max(arr, step = 1):
    n = len(arr) 
    comps = 0
    for i in range(0, n, 2 * step):
        comps += 1
        if arr[i] < arr[i + step]:
            for j in range(step):
                swap(arr, i + j, i + j + step)
    if comps == 1:
        return 0, step, comps
    max_index, sec_index, r_comps = r_get_second_max(arr, 2 * step)
    comps += r_comps
    if arr[max_index + step] > arr[sec_index]:
        return max_index, max_index + step, comps + 1
    else:
        return max_index, sec_index, comps + 1
    
def swap(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    
def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./ex1.py filename")
        return
    filename = sys.argv[1]
    arr = init_arr(filename)
    print(get_second_max(arr, True))

if __name__ == "__main__":
    __main__()
