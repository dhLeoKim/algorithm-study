import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)

ret = 0
for i in lst:
    if i <= K:
        a = K//i
        K -= a*i
        ret += a
    
    if N == 0:
        break

print(ret)