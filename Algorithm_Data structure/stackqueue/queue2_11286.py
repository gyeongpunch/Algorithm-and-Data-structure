from queue import PriorityQueue 
import sys
input = sys.stdin.readline
print = sys.stdout.write

data = PriorityQueue()
n = int(input())
for i in range(n):
    a = int(input())
    if a != 0:
        data.put((abs(a), a))
    else:
        if data.empty():
            print('0\n')
        else:
            print(str(data.get()[1]) + '\n')
