def solution(tickets):
    N = len(tickets)
    visited = [False]*N
    ret = []

    def dfs(now, path):
        if len(path) == N+1:
            ret.append(path)
            return

        for i in range(N):
            if not visited[i] and now == tickets[i][0]:
                visited[i] = True
                dfs(tickets[i][1], path+[tickets[i][1]])
                visited[i] = False

    dfs('ICN', ['ICN'])
    ret.sort()

    return ret[0]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))