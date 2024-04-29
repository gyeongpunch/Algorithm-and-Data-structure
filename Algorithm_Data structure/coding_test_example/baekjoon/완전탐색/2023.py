import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)

n = int(input())

def IsPrime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            else:
                if IsPrime(number * 10 + i):
                    DFS(number * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)