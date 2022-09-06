import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def DFS(i, j, color):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        visited[i][j] = True
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            

N = int(input())
lst = [list(input().strip()) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            DFS(i, j, lst[i][j])