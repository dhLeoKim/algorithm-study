from heapq import heappush, heappop

def solution(n, costs):
    
    def prim(start):
        visited[start] = True
        ret = 0
        h = []
        for w, v in graph[start]:
            heappush(h, (w, v))

        cnt = 0
        while cnt < n-1:
            w, v = heappop(h)
            if visited[v]:
                continue

            ret += w
            visited[v] = True
            cnt += 1
            for nw, nv in graph[v]:
                if not visited[nv]:
                    heappush(h, (nw, nv))

        return ret
    
    graph = [[] for _ in range(n)]
    for u, v, w in costs:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False]*n

    return prim(costs[0][0])

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))