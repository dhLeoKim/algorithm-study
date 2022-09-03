import sys
input = sys.stdin.readline

from collections import deque

def BFS(now):
    queue = deque([now])
    visited[now] = 0
    while queue:
        now = queue.popleft()
        for nxt in [now-1, now+1, 2*now]:
            if nxt < 0 or nxt > 100000 or visited[nxt] != -1: continue
            visited[nxt] = visited[now] + 1
            queue.append(nxt)
            if nxt == K:
                return

N, K = map(int, input().split())
visited = [-1]*(100001)

BFS(N)
print(visited[K])