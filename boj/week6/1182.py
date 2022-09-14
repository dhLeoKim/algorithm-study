import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def subsetSum(idx, local_sum):
    global cnt
    if idx == N:
        if local_sum == S:
            cnt += 1
        return

    subsetSum(idx+1, local_sum)
    subsetSum(idx+1, local_sum + lst[idx])

N, S = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
subsetSum(0, 0)
print(cnt-1) if S == 0 else print(cnt)