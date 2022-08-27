import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    temp = list(map(int, input().split()))
    dice = {                                    # 주사위 정보 저장
        temp[0]: temp[-1], 
        temp[-1]: temp[0],
        temp[1]: temp[3],
        temp[3]: temp[1],
        temp[2]: temp[4],
        temp[4]: temp[2]
        }
    lst.append(dice)

ret = []
for up in range(1, 7):                          # 제일 위 주사위부터 고정후 아래쪽 주사위 탐색
    dice_sum = 0
    i = N-1
    while i >= 0:                               
        count = [0]*7
        down = lst[i][up]                       # 윗 주사위의 아랫면에 해당하는 아랫 주사위면 확인
        
        count[up] = 1
        count[down] = 1
        for k in range(6, 0, -1):               # 아랫주사위의 옆면 중 가장 높은값 sum
            if count[k] == 0:
                dice_sum += k
                break
        up = down
        i -= 1
    ret.append(dice_sum)                        # 경우의 수 저장
print(max(ret))                                 # 경우의 수 중 max값