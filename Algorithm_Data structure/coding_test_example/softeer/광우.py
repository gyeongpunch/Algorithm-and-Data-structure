import sys
input = sys.stdin.readline
from itertools import permutations

N, M, K = map(int, input().split())
data = list(map(int, input().split()))
var_list = permutations(data, N)

result = sys.maxsize

for now_rail in var_list:
    now = list(now_rail)
    
    i = 0
    bucket = 0
    work = 0
    all = 0

    while work < K:
        if bucket + now[i] <= M:
            bucket += now[i]
            now.append(now[i])
            i += 1
        else:
            all += bucket
            bucket = 0
            work += 1
    result = min(result, all)
print(result)

