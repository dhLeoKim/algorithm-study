import sys
sys.stdin = open('input_14499.txt')
input = sys.stdin.readline

N, M, i, j, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice_x = [0, 0, 0, 0]   # 4, 1, 3, 6
dice_y = [0, 0, 0, 0]   # 2, 1, 5, 6

di, dj = [0, 0, -1, 1], [1, -1, 0, 0]

x_idx = 1
y_idx = 1

for command in commands:
    ni, nj = i+di[command-1], j+dj[command-1]

    if ni < 0 or ni > N-1 or nj < 0 or nj > M-1:
        continue

    # 동서남북 이동
    if command == 1:                    # 동
        x_idx = (x_idx+1)%4
        dice_y[y_idx] = dice_x[x_idx]
        dice_y[(y_idx+2)%4] = dice_x[(x_idx+2)%4]
    elif command == 2:                  # 서
        x_idx = (x_idx-1)%4
        dice_y[y_idx] = dice_x[x_idx]
        dice_y[(y_idx+2)%4] = dice_x[(x_idx+2)%4]
    elif command == 3:                  # 북
        y_idx = (y_idx-1)%4
        dice_x[x_idx] = dice_y[y_idx]
        dice_x[(x_idx+2)%4] = dice_y[(y_idx+2)%4]
    elif command == 4:                  # 남
        y_idx = (y_idx+1)%4
        dice_x[x_idx] = dice_y[y_idx]
        dice_x[(x_idx+2)%4] = dice_y[(y_idx+2)%4]
    
    # 주사위 닿은면 갱신
    if lst[ni][nj] == 0:
        lst[ni][nj] = dice_x[x_idx]
    else:
        dice_x[x_idx] = lst[ni][nj]
        dice_y[y_idx] = lst[ni][nj]
        lst[ni][nj] = 0

    i, j = ni, nj

    print(dice_x[(x_idx+2)%4])