#####################
# 1.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def backtracking(k):
    global ret
    if k == N:
        if sum(arr) == S:
            ret += 1
        return
    
    else:
        arr.append(lst[k])
        backtracking(k+1)
        arr.pop()
        backtracking(k+1)
    
N, S = map(int, input().split())
lst = list(map(int, input().split()))

ret = 0
arr = []
backtracking(0)

print(ret-1 if S == 0 else ret)

#####################
# 2.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def backtracking(k, local_sum):
    global ret
    
    if k == N:
        if local_sum == S:
            ret += 1
        return
    
    backtracking(k+1, local_sum + lst[k])
    backtracking(k+1, local_sum)

N, S = map(int, input().split())
lst = list(map(int, input().split()))

ret = 0
backtracking(0, 0)

print(ret-1 if S == 0 else ret)