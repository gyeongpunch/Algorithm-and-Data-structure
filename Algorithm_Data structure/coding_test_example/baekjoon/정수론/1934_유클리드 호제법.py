import sys
input = sys.stdin.readline

n = int(input())

def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)


for _ in range(n):
    A, B = map(int, input().split())
    if A < B:
        A, B = B, A
    print(A * B // GCD(A, B))