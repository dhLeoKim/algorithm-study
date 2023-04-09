import sys
sys.stdin = open('input_11559.txt')
input = sys.stdin.readline

def dfs(si, sj, color):
    global ret, flag
    stack = []
    chain = [(si, sj)]                              # dfs 탐색순서 기록
    stack.append((si, sj))

    while stack:
        i, j = stack.pop()
        for k in range(4):
            ni, nj = i+di[k], j +dj[k]
            if 0 <= ni < 12 and 0 <= nj < 6 and lst[ni][nj] == color and not visited[ni][nj]:
                visited[ni][nj] = True
                chain.append((ni, nj))
                stack.append((ni, nj))

    if len(chain) >= 4:                             # 4칸 확인
        flag = True
        for i, j in chain:
            lst[i][j] = '.'


lst = [list(input().strip()) for _ in range(12)]

di, dj = [1, 0, -1, 0], [0, 1, 0, -1]

ret = 0
flag = True                                         # 폭발 여부
while flag:
    visited = [[False]*6 for _ in range(12)]        # 방문여부 처리로 dfs 중복시작 방지
    flag = False
    for i in range(12):
        for j in range(6):
            if lst[i][j] != '.':
                visited[i][j] = True
                dfs(i, j, lst[i][j])                # 폭발 dfs로 확인

    for j in range(6):                              # 폭발 후 남은 블럭, 아래로 내리기
        row = ''                                    # 문자열로 col 읽은 후 처리
        for i in range(11, -1, -1):
            if lst[i][j] != '.':
                row += lst[i][j]
        row += '.'*(12 - len(row))

        for i in range(11, -1, -1):
            lst[i][j] = row[11-i]

    if flag:                                        # 폭발한 경우 +1
        ret += 1

print(ret)