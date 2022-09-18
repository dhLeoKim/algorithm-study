#################
# 1.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for i in list(combinations(lst, M)):
    print(*i)

#################
# 2.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def backtracking(k, s):
    if k == M:
        print(*arr)
        return

    for i in range(s, N):
        if lst[i] not in arr:
            arr.append(lst[i])
            backtracking(k+1, i)
            arr.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = []
backtracking(0, 0)

#################
# 3.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def backtracking(k):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(k, N):
        if lst[i] not in arr:
            arr.append(lst[i])
            backtracking(i+1)
            arr.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = []
backtracking(0)