import sys
sys.path.append('C:/Users/grege/Python/algorithms-specialization/')

from HuffmanCode import HuffmanCode

def alg(filename):
    with open(filename, 'r') as file:
        huffman = HuffmanCode(file)
    return [huffman.get_height(), huffman.get_min_length()]

def __main__():
    if len(sys.argv) != 2:
        print("usage: python3 ./huffman.py filename")
        return
    filename = sys.argv[1]
    print(alg(filename))

if __name__ == "__main__":
    __main__()