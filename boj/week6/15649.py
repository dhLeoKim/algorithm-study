######################
# 1.

import sys
input = sys.stdin.readline

def dfs():
    if len(stack) == M:
        print(*stack)
        return
    
    else:
        for i in range(1, N+1):
            if i not in stack:
                stack.append(i)
                dfs()
                stack.pop()

N, M = map(int, input().split())

stack = []
dfs()

######################
# 2.

def func(k):
    if k == M:
        print(arr)
        return
    
    else:
        for i in range(1, N+1):
            if not visited[i]:
                arr[k] = i
                visited[i] = True
                func(k+1)
                visited[i] = False

N, M = map(int, input().split())

visited = [False]*(N+1)
arr = [0]*(N+1)
func(0)

######################
# 3.

import sys
input = sys.stdin.readline

from itertools import permutations

N, M = map(int, input().split())

nPr = list(permutations(list(range(1, N+1)), M))

for i in nPr:
    print(*i)