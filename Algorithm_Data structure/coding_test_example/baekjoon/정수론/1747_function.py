import sys
input = sys.stdin.readline

N = int(input())

def IsPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    if IsPrime(N):
        data = list(str(N))
        if data == data[::-1]:
            print(N)
            break
    N += 1