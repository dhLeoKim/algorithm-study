import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from heapq import heappop, heappush

def dijkstra(start):
    h = []
    d[start] = 0
    heappush(h, (0, start))
    while h:
        dist, now = heappop(h)
        if d[now] < dist:
            continue
        for w, nxt in graph[now]:
            ndist = dist + w
            if ndist < d[nxt]:
                d[nxt] = ndist
                heappush(h, (ndist, nxt))

N, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

INF = 1e9
d = [INF]*(N+1)
d[0] = 0

dijkstra(start)
for i in range(1, N+1):
    print('INF' if d[i] == INF else d[i])