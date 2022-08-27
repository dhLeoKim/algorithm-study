import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

LIS = [1]*N     # 커지는 수열
LDS = [1]*N     # 작아지는 수열

for i in range(1, N):
    if lst[i] >= lst[i-1]: LIS[i] = LIS[i-1] + 1        # 크거나 같으면, ++
    if lst[i] <= lst[i-1]: LDS[i] = LDS[i-1] + 1        # 작거나 같으면, ++

print(max(max(LIS), max(LDS)))