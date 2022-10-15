import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

# N : 0 , S : 1
# 시계 : 1, 반시계 : -1

gear = []
for _ in range(4):
    gear.append(deque(map(int, input().strip())))

K = int(input())
lst = [list(map(int, input().split())) for _ in range(K)]

for idx, turn in lst:
    idx -= 1
    r = gear[idx][2]
    l = gear[idx][-2]
    gear[idx].rotate(turn)

    left = idx-1
    right = idx+1
    lturn = rturn = -1*turn

    while right != 4:
        if r == gear[right][-2]:
            break
        r = gear[right][2]
        gear[right].rotate(rturn)
        right += 1
        rturn *= -1

    while left != -1:
        if l == gear[left][2]:
            break
        l = gear[left][-2]
        gear[left].rotate(lturn)
        left -= 1
        lturn *= -1

ret = 0
for i in range(4):
    if gear[i][0]:
        ret += 2**i

print(ret)