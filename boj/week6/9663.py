####################
# 1. 

import sys
input = sys.stdin.readline

def backtracking(j):                            # 좌표 j 선택
    global ret
    if j == N:
        ret += 1
        return

    for i in range(N):                          # 좌표 i 선택
        if not visited_col[i] and not visited_dia1[j+i] and not visited_dia2[j-i+N-1]:
            visited_col[i] = True               # i 확인
            visited_dia1[j+i] = True            # 기울기 -1 대각선 확인
            visited_dia2[j-i+N-1] = True        # 기울기 +1 대각선 (N-1 만큼 평행 이동) 확인
            backtracking(j+1)                   # 다음 j 선택
            visited_col[i] = False
            visited_dia1[j+i] = False
            visited_dia2[j-i+N-1] = False
    
N = int(input())

ret = 0
visited_col = [False]*N
visited_dia1 = [False]*(2*N-1)
visited_dia2 = [False]*(2*N-1)

backtracking(0)
print(ret)


####################
# 2. 

import sys
input = sys.stdin.readline

def promising(j):
    for i in range(j):
        if col[j] == col[i] or abs(col[j] - col[i]) == abs(j - i):
            return False

    return True

def backtracking(j):
    global ret
    if j == N:
        ret += 1
        return
    
    for i in range(N):
        col[j] = i
        if promising(j):
            backtracking(j+1)

N = int(input())

ret = 0
col = [0]*N
backtracking(0)

print(ret)