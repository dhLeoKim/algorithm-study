import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def DFS(now):
    visited[now] = 1
    print(now, end= ' ')
    for nxt in range(N+1):
        if not visited[nxt] and graph[now][nxt] == 1:
            DFS(nxt)

def BFS(now):
    queue = deque([now])
    visited[now] = True
    while queue:
        now = queue.popleft()
        print(now, end= ' ')
        for nxt in range(N+1):
            if not visited[nxt] and graph[now][nxt] == 1:
                visited[nxt] = True
                queue.append(nxt)

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False]*(N+1)
DFS(V)

print()

visited = [False]*(N+1)
BFS(V)