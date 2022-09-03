import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS():
    global queue
    while queue:
        i, j = queue.popleft()
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni > M-1 or nj < 0 or nj > N-1: continue
            if lst[ni][nj] == 0:
                lst[ni][nj] = lst[i][j] + 1
                queue.append((ni, nj))

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]

queue = deque()
for i in range(M):
    for j in range(N):
        if lst[i][j] == 1:
            queue.append((i, j))

BFS()

ret = 0
for row in lst:
    if 0 in row:
        ret = 0
        break
    if max(row) > ret:
        ret = max(row)

print(ret-1)