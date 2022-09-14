import sys
input = sys.stdin.readline

def nQueen(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    
    for i in range(N):
        

N = int(input())
visited = [0]*N
cnt = 0
nQueen(0)