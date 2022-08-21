import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

if K > C*R: print(0)                    # 범위를 벗어나면 0
else:
    sign = [1, 1, -1, -1]               # 방향 부호
    k = -1
    x = 1                               # x, y 좌표
    y = 0
    x_step = C-1                        # step크기
    y_step = R
    num = 0
    flag = False                        # x, y 전환
    while num < K:
        k += 1
        flag = not flag
        if flag:                        # y step만큼 증가
            num += y_step
            y += y_step*sign[k%4]
            y_step -= 1
        else:                           # x step만큼 증가
            num += x_step
            x += x_step*sign[k%4]
            x_step -= 1
    temp = num - K                      # 초과한 만큼 되돌아가기
    if flag: y += temp*-sign[k%4]
    else: x += temp*-sign[k%4]

    print(x, y)