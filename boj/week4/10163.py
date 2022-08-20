import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

M = 1001
arr = [[0]*M for _ in range(M)]

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

# 시간초과??? 
# append 사용하면 초과? 아닌듯! 
# python3 이 문젠듯
# pypy3 으로 하면 통과... 뭐가 문제일까?

ret = [0]*N
for num in range(N-1, -1, -1):                  # 큰수의 색종이부터 채우기
    cnt = 0
    for i in range(lst[num][0], lst[num][0]+lst[num][2]):
        for j in range(lst[num][1], lst[num][1]+lst[num][3]):
            if arr[i][j] == 0:                  # 주어진 영역을 채우고 넓이 바로 계산
                arr[i][j] = num+1
                cnt += 1
    ret[N-1 - num] = cnt                        # 해당 색종이 영역의 넓이를 저장

ret.reverse()                                   # 작은 색종이부터 출력위해 reverse
for i in ret:
    print(i)