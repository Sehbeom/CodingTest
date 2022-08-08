from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*len(graph)

# def BFS(graph, start, visited):
#     deq = deque([start])
#     visited[start] = True

#     while deq:
#         v = deq.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 deq.append(i)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# def BFS(graph, start, visited):
#     # 시작 노드를 큐에다가 먼저 삽입(삽입할 때 파이썬 리스트[]로 감싸주기)
#     queue = deque([start])
#     # 시작 노드를 방문 처리
#     visited[start] = True

#     # 큐에서 노드를 pop하고 그 노드의 인접노드들을 탐색. 단, 큐가 빌(False)때 까지
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)

BFS(graph, 1, visited)