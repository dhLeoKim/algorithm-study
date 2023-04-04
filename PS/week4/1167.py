import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    tmp = list(map(int, input().split()))
    u = tmp[0]
    i = 1
    while tmp[i] != -1:
        graph[u].append((tmp[i], tmp[i+1]))
        i += 2


from collections import deque

def bfs(start):
    visited = [-1]*(N+1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    ret = [0, 0]

    while queue:
        now = queue.popleft()
        for nxt, dist in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + dist
                queue.append(nxt)
                if ret[0] < visited[nxt]:
                    ret = visited[nxt], nxt

    return ret

r, end = bfs(1)
r, end = bfs(end)

print(r)