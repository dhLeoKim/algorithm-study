import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#######################
# 1. prim

from heapq import heappop, heappush

def prim(start):
    ret = 0
    h = []
    MST[start] = True
    for i in range(1, N):
        heappush(h, (graph[start][i], i))

    cnt = 0
    while cnt < N-1:
        cost, now = heappop(h)
        if MST[now]:
            continue
        MST[now] = True
        ret += cost
        cnt += 1
        for nxt in range(N):
            if not MST[nxt] and graph[now][nxt]:
                heappush(h, (graph[now][nxt], nxt))

    return ret

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

MST = [False]*(N+1)

print(prim(0))


#######################
# 2. kruskal

def find(x):
    while p[x] != x:
        x = p[x]
    return x

def union(u, v):
    u = find(u)
    v = find(v)
    if u <= v:
        p[find(v)] = find(u)
    else:
        p[find(u)] = find(v)

def kruskal():
    ret = 0
    
    for w, u, v in edge:
        if find(u) == find(v):
            continue
        ret += w
        union(u, v)

    return ret

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

edge = []
for i in range(N):
    for j in range(i+1, N):
        edge.append((graph[i][j], i, j))

edge.sort()
p = [i for i in range(N)]

print(kruskal())


#######################
# 3. kruskal, union by rank

def find(x):
    if p[x] < 0:
        return x
    else:
        return find(p[x])

def union(u, v):
    u = find(u)
    v = find(v)
    if p[u] == p[v]:
        p[u] -= 1
    if p[u] < p[v]:
        p[v] = u
    else:
        p[u] = v

def kruskal():
    ret = 0
    for w, u ,v in edge:
        if find(u) == find(v):
            continue
        ret += w
        union(u, v)

    return ret

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

edge = []
for i in range(N):
    for j in range(i+1, N):
        edge.append((graph[i][j], i, j))

edge.sort()
p = [-1]*N

print(kruskal())