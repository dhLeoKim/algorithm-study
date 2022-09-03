import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(now):
    queue = deque([now])
    visited[now] = 0
    while queue:
        now = queue.popleft()
        for nxt in [now+U, now-D]:
            if nxt < 1 or nxt > F: continue
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1
                queue.append(nxt)
            if nxt == G:
                return

F, S, G, U, D = map(int, input().split())

visited = [-1]*1000001

BFS(S)
print('use the stairs') if visited[G] == -1 else print(visited[G])