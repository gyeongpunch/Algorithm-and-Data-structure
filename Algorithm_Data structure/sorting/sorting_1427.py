import sys
input = sys.stdin.readline

n = list(input())

for i in range(len(n) - 1):
    max_index = i
    for j in range(i + 1, len(n)):
        if n[max_index] < n[j]:
            max_index = j
    n[i], n[max_index] = n[max_index], n[i]

for i in n:
    print(i, end='')
