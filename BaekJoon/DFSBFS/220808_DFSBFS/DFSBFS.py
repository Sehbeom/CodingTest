from collections import deque

ans_dfs = []
ans_bfs = []

def DFS(graph, n, visited):
    visited[n] = True
    ans_dfs.append(str(n))
    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            DFS(graph, i, visited)

def BFS(graph, n, visited):
    queue = deque([n])
    visited[n] = True

    while queue:
        v = queue.popleft()
        ans_bfs.append(str(v))
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split(' '))
graph = {x : set() for x in range(1, N+1)}

for i in range(1, M+1):
    a, b = map(int, input().split(' '))
    graph[a].add(b)
    graph[b].add(a)

for g in graph:
    graph[g] = list(graph[g])
    graph[g].sort()

DFS(graph, V, [False] * (N+1))
BFS(graph, V, [False] * (N+1))

print(' '.join(ans_dfs))
print(' '.join(ans_bfs))