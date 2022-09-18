####################
# 1.

import sys
input = sys.stdin.readline

def backtracking(k):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(k, N+1):
        if i not in arr:
            arr.append(i)
            backtracking(i+1)
            arr.pop()

N, M = map(int, input().split())

arr = []
backtracking(1)

####################
# 2.

import sys
input = sys.stdin.readline

def backtracking(k, s):
    if k == M:
        print(*arr)
        return
    
    if k != 0:
        s = arr[-1] + 1

    for i in range(s, N+1):
        if i not in arr:
            arr.append(i)
            backtracking(k+1, s)
            arr.pop()

N, M = map(int, input().split())

arr = []
backtracking(0, 1)

####################
# 3.

import sys
input = sys.stdin.readline

def backtracking(k):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(k+1, N+1):
        if i not in arr:
            arr.append(i)
            backtracking(i)
            arr.pop()

N, M = map(int, input().split())

arr = []
backtracking(0)

####################
# 4.

import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())

nCr = list(combinations(list(range(1, N+1)), M))

for i in nCr:
    print(*i)