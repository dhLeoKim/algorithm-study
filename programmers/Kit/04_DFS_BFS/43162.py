from collections import deque

def solution(n, computers):
    visited = [False]*n

    def bfs(now):
        queue = deque([now])
        visited[now] = True

        while queue:
            now = queue.popleft()
            for nxt in range(n):
                if nxt != now and computers[now][nxt] and not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)

    ret= 0
    for computer in range(n):
        if not visited[computer]:
            ret += 1
            bfs(computer)

    return ret


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n, computers))