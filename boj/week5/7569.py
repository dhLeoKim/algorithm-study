import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, H = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

from collections import deque

def BFS():
    global queue
    while queue:
        i, j, k = queue.popleft()
        di = [1, 0, -1, 0, 0, 0]
        dj = [0, 1, 0, -1, 0, 0]
        dk = [0, 0, 0, 0, 1, -1]
        for l in range(6):
            ni = i + di[l]
            nj = j + dj[l]
            nk = k + dk[l]
            if ni < 0 or ni > M-1 or nj < 0 or nj > N-1 or nk < 0 or nk > H-1: continue
            if lst[nk][ni][nj] == 0:
                lst[nk][ni][nj] = lst[k][i][j] + 1
                queue.append((ni, nj, nk))

print(lst)

queue = deque()
for i in range(M):
    for j in range(N):
        for k in range(H):
            if lst[k][i][j] == 1:
                queue.append((i, j, k))

BFS()

ret = 0
for i in range(M):
    for j in range(N):
        for k in range(H):
            if lst[k][i][j] == 0:
                print(-1)
                exit()
            if lst[k][i][j] > ret:
                ret = lst[k][i][j]
print(ret-1)