import sys

sys.setrecursionlimit(2000)

def alg(filename):
    arr = []
    with open(filename, "r") as f:
        for line in f:
            arr.append(int(line))
    return quicksort_compare_all(arr)

def quicksort_compare_all(arr):
    output = []
    for selector in [select_first, select_last, select_median]:
        cpy = arr.copy()
        output.append(quicksort_compare(cpy, selector))
    return output

def quicksort_compare(arr, selector):
    return r_quicksort_compare(arr, 0, len(arr), selector)

def r_quicksort_compare(arr, left, right, selector):
    if right <= left + 1:
        return 0
    pivot = partition(arr, left, right, selector)
    ct = right - left - 1
    ct += r_quicksort_compare(arr, left, pivot, selector)
    ct += r_quicksort_compare(arr, pivot + 1, right, selector)
    return ct

def partition(arr, left, right, selector):
    pivot_index = selector(arr, left, right)
    swap(arr, left, pivot_index)
    pivot = arr[left]
    i = left + 1
    for j in range(left + 1, right):
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1
    swap(arr, left, i - 1)
    return i - 1

def swap(arr, left, right):
    if left == right:
        return
    tmp = arr[left]
    arr[left] = arr[right]
    arr[right] = tmp

def select_first(arr, left, right):
    return left

def select_last(arr, left, right):
    return right - 1

#
# Get the median of three elements in cosntant time
#
def select_median(arr, left, right):
    mid = (left + right - 1) // 2
    indices = [left, mid, right - 1]
    return get_middle_index(arr, indices)

def get_middle_index(arr, indices):
    if len(indices) != 3:
        raise Exception("Can only select middle of three indices")
    sum_indices = len(indices) * (len(indices) - 1) // 2
    curmax = arr[indices[0]]
    maxidx = 0
    curmin = arr[indices[0]]
    minidx = 0
    for i in range(len(indices)):
        if arr[indices[i]] > curmax:
            curmax = arr[indices[i]]
            maxidx = i
        elif arr[indices[i]] < curmin:
            curmin = arr[indices[i]]
            minidx = i
    return indices[sum_indices - minidx - maxidx]
        
    return els[1]
    
def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./quicksort.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()
