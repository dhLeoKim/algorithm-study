import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(sx, sy):
    queue = deque()
    queue.append((sx, sy))
    while queue:
        sx, sy = queue.popleft()
        for i in range(len(nxts)):
            nx, ny = nxts[i]
            if not visited[i] and abs(nx-sx) + abs(ny-sy) <= 1000:
                if nx == ex and ny == ey:
                    return 'happy'
                visited[i] = True
                queue.append((nx, ny))

    return 'sad'

T = int(input())
for case in range(T):
    N = int(input())
    sx, sy = map(int, input().split())
    nxts = [tuple(map(int, input().split())) for _ in range(N)]
    ex, ey = map(int, input().split())
    nxts.append((ex, ey))

    visited = [False]*(N+1)

    print(BFS(sx, sy))