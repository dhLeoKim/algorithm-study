import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    cnt = 1
    while queue:
        i, j = queue.popleft()
        lst[i][j] = 0
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                continue
            if lst[ni][nj] == 1:
                lst[ni][nj] = 0
                queue.append((ni, nj))
                cnt += 1
    
    ret.append(cnt)

# def DFS(i, j):
#     global cnt
#     lst[i][j] = 0
#     di = [1, 0, -1, 0]
#     dj = [0, 1, 0, -1]
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
#             continue
#         if lst[ni][nj] == 1:
#             lst[ni][nj] = 0
#             cnt += 1
#             DFS(ni, nj)

N = int(input())
lst = [list(map(int, input().strip())) for _ in range(N)]

ret = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            BFS(i, j)

            # cnt = 1
            # DFS(i, j)
            # ret.append(cnt)

ret.sort()
print(len(ret))
# print(ret)
for i in ret:
    print(i)