import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# from collections import deque

# def BFS(now):
#     queue = deque([now])
#     visited[now] = 0
#     while queue:
#         now = queue.popleft()
#         for nxt in graph[now]:
#             if nxt == b:
#                 visited[nxt] = visited[now] + 1
#                 return
#             if visited[nxt] == -1:
#                 queue.append(nxt)
#                 visited[nxt] = visited[now] + 1

def DFS(now):
    visited[now] += 1
    if now == b: return
    for nxt in graph[now]:
        if visited[nxt] == -1:
            visited[nxt] = visited[now]
            DFS(nxt)


n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# visited = [-1]*(n+1)
# BFS(a)
# print(visited[b])

visited = [-1]*(n+1)
DFS(a)
print(visited[b])