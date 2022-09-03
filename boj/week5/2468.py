import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(i, j, h):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        i, j = queue.popleft()
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni > N-1 or nj < 0 or nj > N-1 : continue
            if lst[ni][nj] > h and not visited[ni][nj]:
                visited[ni][nj] = True
                queue.append((ni, nj))

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

max_val = 1
for row in lst:
    temp = max(row)
    if temp > max_val:
        max_val = temp

# print(max_val)

ret = []
for h in range(1, max_val):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if lst[i][j] > h and not visited[i][j]:
                BFS(i, j, h)
                cnt += 1
    ret.append(cnt)

# print(ret)

print(max(ret))