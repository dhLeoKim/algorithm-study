def solution(k, dungeons):
    N = len(dungeons)
    visited = [False]*N
    ret = 0

    def dfs(depth, k, num):
        nonlocal ret
        if depth == N:
            if num > ret:
                ret = num
            return

        elif N-depth + num <= ret:
            return

        for i in range(N):
            if not visited[i]:
                visited[i] = True
                if dungeons[i][0] <= k:
                    dfs(depth+1, k-dungeons[i][1], num+1)
                else:
                    dfs(depth+1, k, num)
                visited[i] = False

    dfs(0, k, 0)
    
    return ret

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))