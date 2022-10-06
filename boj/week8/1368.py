import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def find(x):
    if p[x] < 0:
        return x
    return find(p[x])

def union(u, v):
    pu = find(u)
    pv = find(v)
    if p[pu] >= p[pv]:                                          # 비용이 낮은 곳을 대표로 (음수라서 부호 반대)
        p[pv] = pu
    else:
        p[pu] = pv

def kruskal():
    ret = 0
    for w, u, v in edge:
        pu = find(u)
        pv = find(v)
        if pu == pv or (-w < p[pu] and -w < p[pv]):             # 연결하는 것이 직접 우물을 파는 것보다 크면 제외
            continue
        ret += w
        union(u, v)

    return ret

N = int(input())
p = [-int(input()) for _ in range(N)]                           # 직접 파는 비용*(-1)을 parent
graph = [list(map(int, input().split())) for _ in range(N)]

edge = []
for i in range(N):
    for j in range(i+1, N):
        if graph[i][j] >= -p[i] and graph[i][j] >= -p[j]:       # 연결하는 것이 직접 우물을 파는 것보다 크면 제외
            continue
        edge.append((graph[i][j], i, j))

edge.sort()

ret = kruskal()                                                 # 총 연결하는 비용
for i in p:
    if i < 0:                                                   # 직접 파는 비용 더하기
        ret -= i

print(ret)