# MST 구현 : 크루스칼 알고리즘
# * 가장 낮은 비용의 간선부터 오름차순으로 탐색하면서, 간선의 정점들을 합쳐나가는 알고리즘
# * 사이클을 만들지 않으면서, 비용이 작은 간선부터 차례대로 최소 신장 트리에 추가하는 그리디 알고리즘
# * Union Find 자료구조로 구현

# 1. 간선 비용을 오름차순으로 정렬 후, 가장 낮은 비용부터 순서대로 탐색
# 2. 해당 간선이 사이클을 발생한다면 넘어가기
# 3. 해당 간선이 사이클을 발생하지 않는다면 최소 신장 트리에 추가
# 4. 모든 간선에 대해 반복

import sys
sys.stdin = open('re_sample_input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):

    def find_set(x):                                # 대표 원소 찾기
        while rep[x] != x:
            x = rep[x]
        return x

    def union(x, y):                                # 대표 원소 바꾸기
        rep[find_set(y)] = find_set(x)

    def kruskal():
        cnt = 0
        ret = 0
        for w, u, v in edge:                        # 간선 중에서
            if find_set(u) != find_set(v):          # 사이클을 형성하지 않으면
                cnt += 1
                union(u, v)                         # 대표 원소 바꾸기
                ret += w                            # 가중치 더하기
                if cnt == N-1:
                    return ret


    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    edge = []
    for i in range(N):
        for j in range(i+1, N):
            L = (X[i] - X[j])**2 + (Y[i] - Y[j])**2
            edge.append((E*L, i, j))

    edge.sort()
    rep = [i for i in range(N)]                   # 대표원소 초기화

    ret = kruskal()

    print(f'#{tc} {ret:.0f}')