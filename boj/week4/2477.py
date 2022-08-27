import sys
sys.stdin = open('input2.txt')
intput = sys.stdin.readline

K = int(input())
direction = [[1, 3], [4, 1], [2, 4], [3, 2]]    # 'ㄱ' 자 구간 확인 배열
big = [[], []]                                  # 이동방향이 [1, 3], [4, 1], [2, 4], [3, 2] 이면 'ㄱ' 구간
small = [[], []]
prev = [0, 0]
for _ in range(6):
    a, b = map(int, input().split())
    big[a//3].append(b)                         # 가로(1, 2), 세로(3, 4) 구분
    small[0].append(a)                          # 이동방향 저장
    small[1].append(b)

small[0].append(small[0][0])                    # 시작점 마지막에 추가
small[1].append(small[1][0])

for i in range(6):                              
    if small[0][i:i+2] in direction:            # 이동방향 이 'ㄱ'자 이면
        s = small[1][i]*small[1][i+1]           # 'ㄱ'구간 넓이 계산
        break

print(K * (max(big[0])*max(big[1]) - s))        # 전체에서 'ㄱ'구간 빼기