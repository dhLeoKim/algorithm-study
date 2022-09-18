#################
# 1.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from itertools import permutations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for i in list(permutations(lst, M)):
    print(*i)

#################
# 2.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def backtracking(k):
    if k == M:
        print(*arr)
        return
    
    for i in lst:
        if i not in arr:
            arr.append(i)
            backtracking(k+1)
            arr.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = []
backtracking(0)