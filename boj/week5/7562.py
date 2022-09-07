import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    board[i][j] = 0
    while queue:
        i, j = queue.popleft()
        di = [-2, -1, 1, 2, 2, 1, -1, -2]
        dj = [1, 2, 2, 1, -1, -2, -2, -1]
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni < N and 0 <= nj < N and board[ni][nj] == -1:
                board[ni][nj] = board[i][j] + 1
                queue.append((ni, nj))
                if (ni, nj) == (ei, ej):
                    return

T = int(input())
for case in range(T):
    N = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    board = [[-1]*N for _ in range(N)]

    BFS(si, sj)

    print(board[ei][ej])
    # for row in board:
    #     print(row)