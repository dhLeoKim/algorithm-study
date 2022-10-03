import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#########################
# 1. prim

from heapq import heappop, heappush

def prim(start):
    visited[start] = True
    h = []
    for w, v in graph[start]:
        heappush(h, (w, v))

    ret = 0
    cnt = 0
    while cnt < N-1:
        w, v = heappop(h)
        if visited[v]:
            continue

        ret += w
        visited[v] = True

        for nw, nv in graph[v]:
            if not visited[nv]:
                heappush(h, (nw, nv))

        cnt += 1

    return ret

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

visited = [False]*(N+1)
print(prim(u))

#########################
# 2. kruskal

def find(x):
    while p[x] != x:
        x = p[x]
    return x

def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu <= pv:
        p[pv] = pu
    else:
        p[pu] = pv

def kruskal():
    ret = 0
    for w, u, v in edge:
        if find(u) != find(v):
            ret += w
            union(u, v)

    return ret

N, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((w, u, v))

edge.sort()

p = [i for i in range(N+1)]

print(kruskal())


#########################
# 3. kruskal

def find(x):                                    # 부모 찾기
    if p[x] < 0:
        return x
    return find(p[x])

def union(u, v):                                # 합치기
    pu = find(u)
    pv = find(v)
    if p[pu] == p[pv]:                          # 랭크가 같다면 한쪽을 -1
        p[pu] -= 1
    if p[pu] < p[pv]:                           # 랭크가 낮은 쪽으로 합치기
        p[pv] = pu
    else:
        p[pu] = pv

def kruskal():
    ret = 0
    for w, u, v in edge:
        if find(u) == find(v):                  # 같은 그룹이면 continue
            continue
        ret += w                                # 다른 그룹이면 최소 신장 트리 추가
        union(u, v)                             # 같은 그룹으로 변경

    return ret

N, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((w, u, v))                      # 간선 배열

edge.sort()                                     # 비용 기준으로 오름차순
p = [-1]*(N+1)                                  # 부모 배열, rank -1로 초기화

print(kruskal())