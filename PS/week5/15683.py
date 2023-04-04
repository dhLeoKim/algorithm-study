import sys
sys.stdin = open('input_15683.txt')
input = sys.stdin.readline

from collections import deque

# cctv으로 포함되는 영역 처리
def bfs_plus(si, sj, direction):
    tmp = 0
    queue = deque()

    for di, dj in direction:
        queue.append((si, sj))
        while queue:
            i, j = queue.popleft()
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M:
                if lst[ni][nj] == 6:
                    continue
                elif lst[ni][nj] == 0:
                    lst[ni][nj] = -1
                    tmp += 1

                queue.append((ni, nj))

    return tmp


# 완전탐색
def dfs(idx, res):
    global res_max, lst

    if idx == K:                                            # cctv가 포함하는 최대영역의 값 업데이트
        if res > res_max:
            res_max = res
        return
    
    case, si, sj = cctv[idx]

    prev_lst = []                                           # lst 임시 저장
    for i in range(N):
        prev_lst.append(lst[i][:])

    # cctv 종류 별로 분류해서 처리
    if case == 1:
        for k in range(4):                                  # 1번 cctv 방향 정의
            direction = [(di[k], dj[k])]
            tmp = bfs_plus(si, sj, direction)               # cctv 영역 계산

            dfs(idx+1, res+tmp)                             # 다음 재귀

            lst = []                                        # 되돌리기
            for i in range(N):
                lst.append(prev_lst[i][:])

    elif case == 2:
        for k in range(2):
            direction = [(di[k], dj[k]), (di[k+2], dj[k+2])]
            tmp = bfs_plus(si, sj, direction)

            dfs(idx+1, res+tmp)

            lst = []
            for i in range(N):
                lst.append(prev_lst[i][:])

    elif case == 3:
        for k in range(4):
            direction = [(di[k], dj[k]), (di[(k+1)%4], dj[(k+1)%4])]
            tmp = bfs_plus(si, sj, direction)

            dfs(idx+1, res+tmp)

            lst = []
            for i in range(N):
                lst.append(prev_lst[i][:])

    elif case == 4:
        for k in range(4):
            direction = []
            for l in range(4):
                if k == l:
                    continue
                direction.append((di[l], dj[l]))
            tmp = bfs_plus(si, sj, direction)

            dfs(idx+1, res+tmp)

            lst = []
            for i in range(N):
                lst.append(prev_lst[i][:])

    elif case == 5:
        direction = []
        for k in range(4):
            direction.append((di[k], dj[k]))
        tmp = bfs_plus(si, sj, direction)

        dfs(idx+1, res+tmp)

        lst = []
        for i in range(N):
            lst.append(prev_lst[i][:])


N, M = map(int, input().split())
wall = []
cctv = []
lst = []
for i in range(N):
    row = list(map(int, input().split()))
    lst.append(row)
    for j in range(M):
        if row[j] == 6:
            wall.append((i, j))
        elif row[j]:
            cctv.append((row[j], i, j))

K = len(cctv)
di, dj = [0, 1, 0, -1] , [1, 0, -1, 0]
ret = N*M - K - len(wall)                                       # 0 의 개수
res_max = 0                                                     # cctv 영역 최대 개수
dfs(0, 0)

ret = ret - res_max
print(ret)