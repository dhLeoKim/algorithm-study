import sys
sys.stdin = open('input_14502.txt')
input = sys.stdin.readline

from collections import deque

def bfs(start):
    i, j = start
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    cnt = 1
    flag = True

    while queue:
        i, j = queue.popleft()
        if lst[i][j] == 2:
            flag = False
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and lst[ni][nj] != 1:
                visited[ni][nj] = True
                queue.append((ni, nj))
                cnt += 1

    return cnt if flag else 0


def dfs(chk):
    global ret, visited
    if chk == 3:                                    # 벽을 다 세운 후, BFS로 안전지역 갯수 세기
        total = 0
        visited = [[False]*M for _ in range(N)]
        for vi in range(N):
            for vj in range(M):
                if not visited[vi][vj] and lst[vi][vj] == 0:
                    total += bfs((vi, vj))

        if total > ret:
            ret = total
        return

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 0:
                lst[i][j] = 1
                dfs(chk+1)
                lst[i][j] = 0  


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
ret = 0

dfs(0)                                              # 벽을 세울 3곳 완전탐색

print(ret)