import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start):
    global ret
    visited = [[False]*N for _ in range(N)]
    i, j = start
    queue = deque()
    queue.append([i, j ,0])
    visited[i][j] = True
    depth = 1
    di, dj = [-1, 0, 0, 1], [0, -1, 1, 0]
    while queue:
        i, j, d = queue.popleft()
        if lst[i][j] and lst[i][j] < shark[0]:
            ret += d
            lst[i][j] = 0
            shark[1] += 1
            if shark[0] == shark[1]:
                shark[0] += 1
                shark[1] = 0
            visited = [[False]*N for _ in range(N)]
            visited[i][j] = True
            queue = deque()
            queue.append([i, j, 0])
            continue
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and lst[ni][nj] <= shark[0]:
                visited[ni][nj] = True
                queue.append([ni, nj, d+1])
        

N = int(input())
lst = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 9:
            start = [i, j]
            temp[j] = 0
    lst.append(temp)

ret = 0
shark = [2, 0]

bfs(start)

print(ret)