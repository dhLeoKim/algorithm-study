from collections import deque

def solution(n, edge):

    def bfs(now):
        queue = deque()
        queue.append(now)
        visited[now] = 0
        while queue:
            now = queue.popleft()
            for nxt in adj[now]:
                if visited[nxt] == -1:
                    queue.append(nxt)
                    visited[nxt] = visited[now] + 1
    
    
    adj = [[]*(n+1) for _ in range(n+1)]

    for u, v in edge:
        adj[u].append(v)
        adj[v].append(u)

    visited = [-1]*(n+1)
    bfs(1)

    print(visited)

    maxd = 0
    ret = 0
    for dis in visited:
        if dis > maxd:
            maxd = dis
            ret = 1
        elif dis == maxd:
            ret += 1

    return ret


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))


# 테스트 1 〉	통과 (0.07ms, 7.82MB)
# 테스트 2 〉	통과 (0.04ms, 7.62MB)
# 테스트 3 〉	통과 (0.07ms, 7.7MB)
# 테스트 4 〉	통과 (0.29ms, 7.73MB)
# 테스트 5 〉	통과 (1.02ms, 7.96MB)
# 테스트 6 〉	통과 (1.74ms, 8.77MB)
# 테스트 7 〉	통과 (21.26ms, 16.1MB)
# 테스트 8 〉	통과 (56.43ms, 20.4MB)
# 테스트 9 〉	통과 (51.87ms, 20.5MB)