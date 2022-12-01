from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    visited = [[False]*M for _ in range(N)]

    def bfs():
        di, dj = [0, 1, 0, -1], [1, 0, -1, 0]

        queue = deque()
        queue.append((0, 0, 1))
        visited[0][0] = True
        
        while queue:
            i, j, l = queue.popleft()

            if i == N-1 and j == M-1:
                return l

            for k in range(4):
                ni, nj = i+di[k], j+dj[k]

                if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj, l+1))

        return -1
    
    ret = bfs()

    return ret

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

print(solution(maps))