import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

window = 0
for i in range(K):
    window += lst[i]

max_v = window
for i in range(N-K):
    window += lst[i+K] - lst[i]

    if window > max_v:
        max_v = window

print(max_v)