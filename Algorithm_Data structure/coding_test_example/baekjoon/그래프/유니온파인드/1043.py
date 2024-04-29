import sys
input = sys.stdin.readline

N, M = map(int, input().split())
truth = list(map(int, input().split()))
T = truth[0]
del truth[0]
answer = 0
parent = [i for i in range(N + 1)]
party = [[] for _ in range(M)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(M):
    people = list(map(int, input().split()))
    party[i] = people[1:]

# print('parent 는', parent)
# print('party는' , *party, sep = '\n')

for i in range(M):
    firstPeople = party[i][0]
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])

for i in range(M):
    isPossible = True
    firstPeople = party[i][0]
    for j in range(len(truth)):
        if find(firstPeople) == find(truth[j]):
            isPossible = False
            break
    if isPossible:
        answer += 1
print(answer)