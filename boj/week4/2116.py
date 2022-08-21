import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    temp = list(map(int, input().split()))
    dice = {
        temp[0]: temp[-1], 
        temp[-1]: temp[0],
        temp[1]: temp[3],
        temp[3]: temp[1],
        temp[2]: temp[4],
        temp[4]: temp[2]
        }
    lst.append(dice)

ret = []
for up in range(1, 7):
    dice_sum = 0
    i = N-1
    while i >= 0:
        count = [0]*7
        down = lst[i][up]
        
        count[up] = 1
        count[down] = 1
        for k in range(6, 0, -1):
            if count[k] == 0:
                dice_sum += k
                break
        up = down
        i -= 1
    ret.append(dice_sum)
print(max(ret))