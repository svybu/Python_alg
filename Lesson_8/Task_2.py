"""Закодируйте любую строку из трех слов по алгоритму Хаффмана."""
from collections import Counter
import heapq

s = 'quod erat demonstrandum'
class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def go(self, code_dict, path):
        self.left.go(code_dict, path + "0")
        self.right.go(code_dict, path + "1")

class Leaf:
    def __init__(self, value):
        self.value = value

    def go(self, code_dict, path):
        code_dict[self.value] = path
        return path

def huffmans(s):
    arr = []
    for i, j in Counter(s).items():
        arr.append((j, len(arr), Leaf(i)))
        repeat = len(arr)
        heapq.heapify(arr)
        while len(arr) > 1:
            a = heapq.heappop(arr)
            b = heapq.heappop(arr)
            heapq.heappush(arr, (a[0]+b[0], repeat, Node(a[2], b[2])))
            repeat += 1

    result = {}
    if arr:
        arr[0][2].go(result, '')
    return result

s = Counter(s)

d = huffmans(s)
for e, elem in d.items():
    print(f'{e} : {elem}\n')