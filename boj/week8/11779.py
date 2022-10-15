import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from heapq import heappop, heappush

def dijsktra(start):
    h = []
    d[start] = 0
    heappush(h, (0, start))
    while h:
        dist, u = heappop(h)
        if d[u] < dist:
            continue
        for v, w in graph[u]:
            ndist = dist + w
            if ndist < d[v]:
                d[v] = ndist
                heappush(h, (ndist, v))
                pre[v] = u

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
s, e = map(int, input().split())

INF = 1e9
d = [INF]*(N+1)
pre = [0]*(N+1)

dijsktra(s)
print(d[e])

now = e
ret = []
while now != 0:
    ret.append(now)
    now = pre[now]

print(len(ret))
print(*ret[::-1])