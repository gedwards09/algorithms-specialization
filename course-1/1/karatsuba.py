import sys

#
# Implement karatsuba multiplication
#
def k_multiply(x, y):
    if y > x:
        return k_multiply(y, x)
    sx = str(x)
    xlen = len(str(x))
    if xlen <= 1:
        return x * y
    sy = justify(y, xlen)
    mid = xlen // 2
    a = int(sx[:mid])
    b = int(sx[mid:])
    c = int(sy[:mid])
    d = int(sy[mid:])
    ac = k_multiply(a, c)
    bd = k_multiply(b, d)
    cross = k_multiply(a + b, c + d) - ac - bd
    nshift = xlen - mid
    return shift_digits(ac, 2 * nshift) + shift_digits(cross, nshift) + bd

#
# Justify integer to specified length by prepending zeros
# returns: zero-prepended integer as string
#
def justify(x, sz):
    sx = str(x)
    return ''.join(['0' for _ in range(sz - len(sx))]) + sx

#
# Shift integer by appending zeros to the end
# returns: zero-shifted integer as numeric
#
def shift_digits(x, nzeros):
    return int(str(x) + ''.join(['0' for _ in range(nzeros)]))

#
# Entry pointer for tester script
#
def alg(filename):
    with open(filename, "r") as f:
        x = int(f.readline())
        y = int(f.readline())
    return k_multiply(x, y)

#
# Entry point for command line execution
#
def __main__():
    if len(sys.argv) != 2:
        print("usage: python ./karatsuba.py [filename]")
        return
    print(alg(sys.argv[1]))

if __name__ == "__main__":
    __main__()