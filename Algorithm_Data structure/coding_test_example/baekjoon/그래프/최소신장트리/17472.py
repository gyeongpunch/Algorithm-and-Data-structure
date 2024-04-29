import sys
input = sys.stdin.readline
import copy
from collections import deque
from queue import PriorityQueue

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())

visited = [[False for j in range(M)] for i in range(N)]
A = [[] for _ in range(N)]
for i in range(N):
    data = list(map(int, input().split()))
    A[i] = data
print(*A, sep = '\n')

sNum = 1
sumlist = list([])
mlist = []

def addNode(i, j, queue):
    A[i][j] = 