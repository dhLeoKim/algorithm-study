import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

LIS = [1]*N
LDS = [1]*N

for i in range(1, N):
    if lst[i] >= lst[i-1]: LIS[i] = LIS[i-1] + 1
    if lst[i] <= lst[i-1]: LDS[i] = LDS[i-1] + 1

print(max(max(LIS), max(LDS)))