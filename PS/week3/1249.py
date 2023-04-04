# 다익스트라 알고리즘
# 하나의 시작 정점에서 다른 모든 정점으로 가는 최단 경로 계산
# 매 정점마다 가장 적은 비용이 드는 정점을 선택하는 그리디 알고리즘
# 음의 간선이 없을 때 사용

# 1. 방문하지 않은 정점 중, 현재 정점에서의 최단 거리가 가장 짧은 정점 선택
# 2. 해당 정점을 거쳐 다른 정점으로 가는 비용을 계산하여 최소값 테이블에 업데이트
# 3. 모든 정점에 대해 반복

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):

    from heapq import heappop, heappush

    def dijkstra(start):
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        i, j = start
        h = []                                          # 최소힙
        d[i][j] = 0                                     # 시작점
        heappush(h, (0, i, j))
        while h:
            dist, i, j = heappop(h)                     # 최소 비용 간선 선택
            if d[i][j] < dist:                          # 해당 간선을 거쳐 가는 비용(dist)이 현재까지의 최소값(테이블에 저장된 최소값) 보다 크면 continue
                continue
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]               # 다음 인근 정점
                if 0 <= ni < N and 0 <= nj < N:
                    ndist = dist + lst[ni][nj]          # 다음 노드로 가는 비용 계산
                    if d[ni][nj] > ndist:
                        d[ni][nj] = ndist               # 최소값이면 테이블 업데이트 후
                        heappush(h, (ndist, ni, nj))    # 힙에 추가


    N = int(input())
    lst = [list(map(int, list(input().strip()))) for _ in range(N)]

    INF = 1e9
    d = [[INF]*N for _ in range(N)]

    dijkstra((0, 0))    

    print(f'#{tc}', d[N-1][N-1])