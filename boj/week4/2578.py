import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(5)]
# list comprehension으로 한번에 받는 방법 찾아보기!
lst = []
for _ in range(5):
    lst.extend(map(int, input().split()))   # extend 혹은 lst += temp
    # lst += list(map(int, input().split()))

num = {}                        
for i in range(5):                          # 빙고 좌표 저장
    for j in range(5):
        num[arr[i][j]] = [i, j]

row = [[0]*5 for _ in range(5)]             # 빙고 판단할 배열 초기화
col = [[0]*5 for _ in range(5)]
diag = [[0]*5 for _ in range(2)]

cnt = 0
for k in lst:                               # 빙고 채우기
    i, j = num[k]
    row[i][j] = 1
    if sum(row[i]) == 5: cnt += 1           # 해당되는 가로, 세로, 대각선만 확인
    col[j][i] = 1
    if sum(col[j]) == 5: cnt += 1
    if i == j: 
        diag[0][j] = 1
        if sum(diag[0]) == 5: cnt += 1
    if i+j == 4: 
        diag[1][j] = 1
        if sum(diag[1]) == 5: cnt += 1

    if cnt >= 3:                            # 빙고가 3개이상이면 승리
        print(lst.index(k)+1)
        break