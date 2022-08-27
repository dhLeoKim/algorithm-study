import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

d = [0]*(N-K+1)
d[0] = sum(lst[:K])                             # d : K구간 합을 저장
for i in range(1, N-K+1):
    d[i] = d[i-1] - lst[i-1] + lst[i+K-1]       # d : 다음 칸 더하고 이전 칸 빼기
print(max(d))