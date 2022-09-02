import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    lst[i][j] = 2
    while queue:
        i, j = queue.popleft()
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni > N-1 or nj < 0 or nj > M-1:
                continue
            if lst[ni][nj] == 1:
                lst[ni][nj] = lst[i][j] + 1
                queue.append((ni, nj))
            if ni == N-1 and nj == M-1:
                return
    return

N, M = map(int, input().split())
lst = [list(map(int, list(input().strip()))) for _ in range(N)]

BFS(0,0)
print(lst[N-1][M-1]-1)