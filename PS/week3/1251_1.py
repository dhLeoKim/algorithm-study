# MST 구현 : 프림 알고리즘
# * 하나의 정점에서 연결된 간선들 중 최소 비용의 간선을 선택해나가는 알고리즘
# * 임의의 한 점에서 시작해서, 매번 가장 낮은 비용의 간선을 선택해서 뻗어나가는 그리디 알고리즘
# * 운선 순위 큐로 구현

# 1. 임의의 정점 선택해서 최소 신장 트리에 추가
# 2. 최소 신장 트리에 포함된 정점에서 포함되지 않은 인접 정점을 연결하는 간선들 중,
# 3. 비용이 가장 작은 간선을 선택하여 연결되는 정점을 최소 신장 트리에 추가
# 4. 최소 신장 트리에 V-1개의 간선이 추가될 때 까지 반복

import sys
sys.stdin = open('re_sample_input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):

    from heapq import*

    def prim(start):
        visited[start] = True
        ret = 0
        h = []
        for w, v in graph[start]:
            heappush(h, (w, v))             # u와 연결된 간선 우선순위 큐 추가

        cnt = 0
        while cnt < N-1:                    # N-1개의 간선이 추가될 때 까지 반복
            w, v = heappop(h)
            if visited[v]:                  # 최소신장트리에 포함된 정점을 연결하는 간선이면 continue
                continue
            ret += w                        # 포함되지 않은 정점을 연결하는 간선이면, 최소신장트리에 추가
            visited[v] = True
            cnt += 1
            for nw, nv in graph[v]:
                if not visited[nv]:         # 최소 신장 트리에 포함되지 않은 정점을 연결하는 모든 간선을
                    heappush(h, (nw, nv))   # 우선순위 큐에 추가

        return ret


    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            L = (X[i] - X[j])**2 + (Y[i] - Y[j])**2
            graph[i].append((E*L, j))
            graph[j].append((E*L, i))

    visited = [False]*N
    ret = prim(0)


    print(f'#{tc} {ret:.0f}')