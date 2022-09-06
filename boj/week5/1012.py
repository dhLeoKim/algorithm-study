import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#########
# # 1. BFS
# from collections import deque

# def BFS(i, j):
#     queue = deque()
#     queue.append((i, j))
#     lst[i][j] = 0
#     while queue:
#         i, j = queue.popleft()
#         di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
#         for k in range(4):
#             ni, nj = i + di[k], j + dj[k]
#             if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 1:
#                 queue.append((ni, nj))
#                 lst[ni][nj] = 0

# T = int(input())
# for case in range(T):
#     M, N, K = map(int, input().split())
#     lst = [[0]*M for _ in range(N)]
#     for _ in range(K):
#         j, i = map(int, input().split())
#         lst[i][j] = 1
    
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if lst[i][j] == 1:
#                 BFS(i, j)
#                 cnt += 1

#     print(cnt)

#########
# # 2. DFS
def DFS(i, j):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        lst[i][j] = 0                               # 방문처리 위치 조심
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 1:
                stack.append((ni, nj))

T = int(input())
for case in range(T):
    M, N, K = map(int, input().split())
    lst = [[0]*M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        lst[i][j] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                # lst[i][j] = 0
                DFS(i, j)
                cnt += 1

    print(cnt)