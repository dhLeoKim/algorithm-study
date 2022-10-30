import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]
lst = [input().strip() for _ in range(M)]

R = 1
idx = 2
MX = 501
chk = [False]*MX
nxt = [[-1]*26 for _ in range(MX)]


def insert(S):
    global idx

    for s in S:
        now = R
        for c in s:
            cidx = ord(c) - ord('a')
            if nxt[now][cidx] == -1:
                nxt[now][cidx] = idx
                idx += 1
            now = nxt[now][cidx]
        chk[now] = True


def find(S):
    ret = 0
    for s in S:
        now = R
        for c in s:
            cidx = ord(c) - ord('a')
            if nxt[now][cidx] == -1:
                break
            now = nxt[now][cidx]
        
        if chk[now]:
            ret += 1    
    return ret

insert(S)
print(find(lst))