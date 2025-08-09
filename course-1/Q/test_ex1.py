import random
import ex1

random.seed(999)

def __main__():
    for i in range(1, 11):
        arr = [random.randint(0, 2 ** i) for _ in range(2 ** i)]
        arr.sort()
        exp_max = arr[-1]
        exp_sec = arr[-2]
        exp_comps = 2 ** i + i - 2
        for i in range(20):
            arr = permute(arr)
            max_, sec, comps = ex1.r_get_second_max(arr)
            assert arr[max_] == exp_max
            assert arr[sec] == exp_sec
            assert int(comps) == exp_comps

def permute(arr):
    n = len(arr)
    for i in range(n):
        ex1.swap(arr, i, random.randint(i, n - 1))
    return arr

if __name__ == "__main__":
    __main__()