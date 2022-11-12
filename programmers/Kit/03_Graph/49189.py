from heapq import heappush, heappop

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for u, v in edge:
        graph[u].append((v, 1))
        graph[v].append((u, 1))

    INF = 1e9
    d = [INF]*(n+1)

    h = []
    d[0] = 0
    d[1] = 0
    heappush(h, (0, 1))

    while h:
        du, u = heappop(h)
        if d[u] < du:
            continue
        for v, w in graph[u]:
            dv = du + w
            if dv < d[v]:
                d[v] = dv
                heappush(h, (dv, v))

    print(d)
    maxd = 0
    ret = 0
    for dis in d:
        if dis > maxd:
            maxd = dis
            ret = 1
        elif dis == maxd:
            ret += 1

    return ret


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))


# 테스트 1 〉	통과 (0.04ms, 7.62MB)
# 테스트 2 〉	통과 (0.03ms, 7.88MB)
# 테스트 3 〉	통과 (0.06ms, 7.67MB)
# 테스트 4 〉	통과 (0.45ms, 7.83MB)
# 테스트 5 〉	통과 (2.10ms, 8.09MB)
# 테스트 6 〉	통과 (4.67ms, 9.46MB)
# 테스트 7 〉	통과 (53.89ms, 21.7MB)
# 테스트 8 〉	통과 (90.80ms, 28.1MB)
# 테스트 9 〉	통과 (137.36ms, 28.8MB)