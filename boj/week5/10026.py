import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(i, j, color):
    q1 = deque()
    q1.append((i, j))
    visited1[i][j] = True
    while q1:
        i, j = q1.popleft()
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0<= ni < N and 0<= nj < N and not visited1[ni][nj] and lst[ni][nj] == color:
                q1.append((ni, nj))
                visited1[ni][nj] = True

def BFS2(i, j, color):
    q2 = deque()
    q2.append((i, j))
    visited2[i][j] = True
    while q2:
        i, j = q2.popleft()
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0<= ni < N and 0<= nj < N and not visited2[ni][nj]:
                if lst[ni][nj] == color or (color != 'B' and lst[ni][nj] != 'B'):
                    q2.append((ni, nj))
                    visited2[ni][nj] = True

N = int(input())
lst = [list(input().strip()) for _ in range(N)]

visited1 = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]

cnt1 = cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            BFS(i, j, lst[i][j])
            cnt1 += 1
        if not visited2[i][j]:
            BFS2(i, j, lst[i][j])
            cnt2 += 1

print(cnt1, cnt2)