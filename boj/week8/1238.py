import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from heapq import heappop, heappush

def dijkstra(start):
    h = []
    d[start][start] = 0
    heappush(h, (0, start))
    while h:
        dist, now = heappop(h)

        if dist > d[start][now]:
            continue
        
        for w, nxt in graph[now]:
            ndist = dist + w
            if ndist < d[start][nxt]:
                d[start][nxt] = ndist
                heappush(h, (ndist, nxt))


N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

INF = 1e9
d = [[INF]*(N+1) for _ in range(N+1)]

for s in range(1, N+1):
    dijkstra(s)

ret = 0
for i in range(1, N+1):
    temp = d[i][X] + d[X][i]
    if temp > ret:
        ret = temp

print(ret)

# 그래프 방향 반대로 저장하여 한번 더 다익스트라! 총 2번이면 해결