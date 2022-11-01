from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    
    def dijkstra(start):
        h = []
        d[start][start] = 0
        heappush(h, (0, start))
        while h:
            du, u = heappop(h)
            if d[start][u] < du:
                continue
            for v, w in graph[u]:
                dv = du + w
                if dv < d[start][v]:
                    d[start][v] = dv
                    heappush(h, (dv, v))
    
    graph = [[] for _ in range(n+1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    INF = 1e9
    d = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dijkstra(i)

    ret = INF
    for i in range(1, n+1):
        temp = d[s][i] + d[i][a] + d[i][b]
        if temp < ret:
            ret = temp

    return ret