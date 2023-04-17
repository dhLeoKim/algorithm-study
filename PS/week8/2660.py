import sys
sys.stdin = open('input_2660.txt')
input = sys.stdin.readline

from collections import deque

def bfs(now):
    visited = [-1]*(N+1)
    visited[now] += 1
    queue = deque()
    queue.append(now)

    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + 1             # visited 에 깊이 저장
                queue.append(nxt)

    return max(visited)                                     # 최대 깊이 반환


N = int(input())
graph = [[] for _ in range(N+1)]
while True:                                                 # 그래프 저장
    u, v = map(int, input().split())
    if u == -1 and v == -1: 
        break

    graph[u].append(v)
    graph[v].append(u)

ret = 50
candidate = []
for i in range(1, N+1):
    score = bfs(i)                                          # bfs로 깊이 계산
    if score < ret:                                         # 최소값 업데이트
        ret = score
        candidate = [i]
    elif score == ret:                                      # 동점자 저장
        candidate.append(i)

print(ret, len(candidate))
print(*candidate)