import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

x, y = map(int, input().split())
N = int(input())
lst = [0]*(N+1)
for i in range(N+1):                        # 위치정보를 좌표로 변환
    a, b = map(int, input().split())
    if a == 1: lst[i] = [b, y, a]
    elif a == 2: lst[i] = [b, 0, a]
    elif a == 3: lst[i] = [0, y-b, a]
    else: lst[i] = [x, y-b, a]

dk = lst.pop()                              # 동근(dk)이의 좌표

ret = 0
for i in range(N):
    if dk[2] + lst[i][2] == 3:                                      # 남북방향일 때
        ret += min(lst[i][0] + dk[0], x-lst[i][0] + x-dk[0]) + y
    elif dk[2] + lst[i][2] == 7:                                    # 동서방향일 때
        ret += min(lst[i][1] + dk[1], y-lst[i][1] + y-dk[1]) + x
    else:                                                           
        ret += abs(lst[i][0] - dk[0]) + abs(lst[i][1] - dk[1])      # 그 외 경우의 길이계산
    # print(ret)

print(ret)


# print(dk, lst, ret)