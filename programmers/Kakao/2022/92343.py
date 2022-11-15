from collections import deque

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for u, v in edges:
        graph[u].append(v)

    visited = [False]*len(info)
    visited[0] = True
    
    ret = 1

    now = 0
    you = [1, 0]
    nxts = set()

    queue = deque()
    queue.append([you, now, nxts])

    while queue:
        you, now, nxts = queue.popleft()
        if you[0] > ret:
            ret = you[0]

        nxts.update(graph[now])

        for nxt in nxts:
            if info[nxt]:
                if you[0] != you[1]:
                    you[1] += 1
                    queue.append([nxt, you, nxts - {nxt}])
            else:
                you[0] += 1
                queue.append([nxt, you, nxts - {nxt}])
                
    return ret

info = [0,0,1,1,1,0,1,0,1,0,1,1]	
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	

# info = [0,1,0,1,1,0,1,0,0,1,0]	
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	

print(solution(info, edges))





# DFS
    # def dfs(you, now):
    #     if you[0] <= you[1]:
    #         return
        
    #     ret.append(you[0])

    #     for nxt in graph[now]:
    #         if visited[now] and not visited[nxt]:
    #             visited[nxt] = True
    #             you[info[nxt]] += 1
    #             dfs(you, now)
    #             dfs(you, nxt)
    #             visited[nxt] = False
    #             you[info[nxt]] -= 1

    # dfs([1, 0], 0)
    # print(ret)