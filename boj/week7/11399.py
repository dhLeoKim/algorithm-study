import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort(reverse= True)

ret = 0
for i in range(N):
    ret += P[i]*(i+1)

print(ret)