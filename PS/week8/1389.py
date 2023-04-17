import sys
sys.stdin = open('input_1389.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start):
    global ret
    visited = [-1]*(N+1)
    visited[start] += 1
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                queue.append(nxt)

    total = sum(visited)
    if total < ret[0]:
        ret = [total, start]

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

ret = [1e11, 0]
for i in range(1, N+1):
    bfs(i)

print(ret[1])