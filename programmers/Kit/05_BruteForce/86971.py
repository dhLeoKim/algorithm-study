from collections import deque

def solution(n, wires):

    def bfs(start):
        queue = deque()
        queue.append(start)
        visited = [False]*(n+1)
        visited[start] = True
        cnt = 0
        while queue:
            now = queue.popleft()
            cnt += 1
            for nxt in adj[now]:
                if not visited[nxt]:
                    queue.append(nxt)
                    visited[nxt] = True

        return cnt

    N = len(wires)
    ret = n
    for i in range(N):
        temp = []
        for wire in wires:
            temp.append(wire[:])
        temp.pop(i)

        adj = [[] for _ in range(n+1)]
        for v1, v2 in temp:
            adj[v1].append(v2)
            adj[v2].append(v1)


        for lst in adj:
            if lst:
                start = lst[0]
                break
        cnt1 = bfs(start)
        cnt2 = n - cnt1

        diff = abs(cnt1 - cnt2)
        if diff < ret:
            ret = diff

    return ret


n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

# n = 4
# wires = [[1,2],[2,3],[3,4]]

# n = 7
# wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

print(solution(n, wires))