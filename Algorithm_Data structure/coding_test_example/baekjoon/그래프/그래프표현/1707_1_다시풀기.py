import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
k = int(input())


def DFS(start, group):
    visited[start] = group  # 현재 노드의 그룹 저장

    for v in A[start]:
        if visited[v] == 0:
            result = DFS(v, -group)
            if not result:
                return False
        else:
            if visited[v] == group:  # 이미 방문한 곳 중에서 노드가 현재 그룹과 같으면 이분 그래프가 아님
                return False
    return True


for _ in range(k):
    V, E = map(int, input().split())
    A = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        A[a].append(b)
        A[b].append(a)

    for i in range(1, V + 1):
        if visited[i] == 0:
            result = DFS(i, 1)
            if not result:
                break
    print("YES") if result else print("NO")