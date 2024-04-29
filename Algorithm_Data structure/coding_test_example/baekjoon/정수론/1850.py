import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

if A < B:
    A, B = B, A
result = ''
n = GCD(A, B)
for _ in range(n):
    print(1, end='')