import sys

def alg(filename):
    array = []
    with open(filename) as f:
        for line in f:
            array.append(int(line))
    return inversions(array, 0, len(array))

def inversions(arr, left, right):
    return merge_sort_inversions(arr, left, right)

def merge_sort_inversions(arr, left, right):
    if right <= left + 1:
        return 0
    inv_ct = 0
    mid = (left + right) // 2
    inv_ct += merge_sort_inversions(arr, left, mid)
    inv_ct += merge_sort_inversions(arr, mid, right)
    inv_ct += merge_inversions(arr, left, mid, right)
    return inv_ct

def merge_inversions(arr, left, mid, right):
    inv_ct = 0
    L = [el for el in arr[left:mid]]
    R = [el for el in arr[mid:right]]
    i = 0
    j = 0
    while left + i < mid and mid + j < right:
        if L[i] > R[j]:
            arr[left + i + j] = R[j]
            inv_ct += mid - left - i
            j += 1
        else:
            arr[left + i + j] = L[i]
            i += 1
    while left + i < mid:
        arr[left + i + j] = L[i]
        i += 1
    while mid + j < right:
        arr[mid + j] = R[j]
        j += 1
    return inv_ct

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./inversions.py [filename]")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()