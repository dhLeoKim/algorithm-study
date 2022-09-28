import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

ret = []
while queue:
    now = queue.popleft()
    ret.append(now)
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

print(*ret)