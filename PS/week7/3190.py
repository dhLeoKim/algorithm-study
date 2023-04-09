import sys
sys.stdin = open('input_3190.txt')
input = sys.stdin.readline

from collections import deque

N = int(input())
K = int(input())

lst = [[0]*N for _ in range(N)]                 # 맵에 사과 표시
for _ in range(K):
    i, j = map(int, input().split())
    lst[i-1][j-1] = 1

L = int(input())
direction = [0]*10005                           # (idx = X)초에 방향 명령 저장
for _ in range(L):
    X, C = input().split()
    direction[int(X)] = C

i, j = 0, 0
lst[i][j] = 2
k = 0
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
snake = deque()
snake.append((i, j))
sec = 0

while True:
    # 방향 명령 확인
    if direction[sec] == 'D':
        k = (k+1)%4
    elif direction[sec] == 'L':
        k = (k-1)%4

    # 다음칸 진행
    ni, nj = i+di[k], j+dj[k]
    if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
        break

    if lst[ni][nj] == 1:                            # 사과
        lst[ni][nj] = 2
        snake.append((ni, nj))
    elif lst[ni][nj] == 0:                          # 빈칸
        lst[ni][nj] = 2
        snake.append((ni, nj))
        ti, tj = snake.popleft()
        lst[ti][tj] = 0
    else:                                           # 자기 몸
        break

    i, j = ni, nj
    sec += 1

sec += 1
print(sec)