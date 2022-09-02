import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(now):
    queue = deque([now])
    visited.append(now)
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if nxt not in visited:
                queue.append(nxt)
                visited.append(nxt)

# def DFS(now):
#     for nxt in graph[now]:
#         if nxt not in visited:
#             visited.append(nxt)
#             DFS(nxt)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = []
BFS(1)
print(len(visited)-1)

# visited = [1]
# DFS(1)
# print(len(visited)-1)
