import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
myque = PriorityQueue()

for i in range(N):
    myque.put(int(input()))

result = 0

while myque.qsize() > 1:
    # print(myque.qsize())
    a = myque.get()
    b = myque.get()
    result += a + b
    # print(myque.qsize())
    myque.put(a + b)
print(result)