import sys
sys.stdin = open('sample_input.txt')
input = sys.stdin.readline

def dfs(idx, core, length):
    global ret
    if idx == M:                                                # 연결할 core후보의 개수 M 만큼, 방향 k 선택해서 경우의 수 생성
        if core > ret[0]:                                       # 완성된 경우의 수에서 core 최대 length 최소 업데이트
            ret = [core, length]
        elif core == ret[0] and length < ret[1]:
            ret = [core, length]
        return
    
    if core + M - idx < ret[0]:                                 # 가지치기 : 앞으로 남은 코어 모두 연결해도 최대값보다 작으면 가지치기
        return

    ci, cj = cell[idx]                                          # idx에 해당하는 core 연결 시작
    for k in range(4):                                          # 방향 선택해서
        i, j = ci, cj
        tmp_length = 0
        while True:                                             # 가장자리까지 연결 시도
            ni, nj = i + di[k], j + dj[k]

            if ni == -1 or ni == N or nj == -1 or nj == N:      # 가장자리에 도착하면, core 연결 length 추가
                core += 1
                length += tmp_length
                break

            if 0 <= ni < N and 0 <= nj < N:
                if lst[ni][nj] == 0:                            # 연결될 전선 2로 표시
                    lst[ni][nj] = 2
                    tmp_length += 1
                else:                                           # 다음 칸으로 연결 불가능하면 break
                    break

            i, j = ni, nj

        dfs(idx+1, core, length)                                # 다음 core후보의 방향 선택

        if i == 0 or i == N-1 or j == 0 or j == N-1:            # 해당 core가 가장자리까지 연결된 경우면, 뺄셈
            length -= tmp_length
            core -= 1
        
        if lst[i][j] == 1:
            continue

        while True:                                             # 연결된 전선 0으로 되돌리기
            lst[i][j] = 0
            ni, nj = i - di[k], j - dj[k]
            if ni == ci and nj == cj:
                break
            i, j = ni, nj


T = int(input())
for tc in range(1, T+1):
    
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    di, dj = [0, -1, 0, 1], [-1, 0, 1, 0]
    cell = []                                                   # 연결할 core 후보, 가장자리 제외

    for i in range(N):
        for j in range(N):
            if lst[i][j] and 0 < i < N-1 and 0 < j < N-1:
                cell.append((i, j))

    M = len(cell)
    ret = [0, 144]                                              # [core 수, 전선길이 합] core 수는 max, 전선길이는 min
    dfs(0, 0, 0)

    print(f'#{tc}', ret[1])