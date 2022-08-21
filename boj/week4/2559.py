import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

d = [0]*(N-K+1)
d[0] = sum(lst[:K])
for i in range(1, N-K+1):
    d[i] = d[i-1] - lst[i-1] + lst[i+K-1]
print(max(d))