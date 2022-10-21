import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from heapq import heappush, heappop, heapify
from collections import deque

N, L = map(int, input().split())
lst = list(map(int, input().split()))

h = []
for i in range(N):
    st = i-L+1
    
    heappush(h, (lst[i], i))

    while h[0][1] < st:
        heappop(h)

    print(h[0][0], end=' ')