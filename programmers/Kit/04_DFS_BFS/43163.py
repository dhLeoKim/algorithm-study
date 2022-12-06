from collections import deque

def solution(begin, target, words):
    N = len(words)

    def bfs():
        visited = [False]*N
        queue = deque()
        queue.append([begin, 0])        

        while queue:
            now, ret = queue.popleft()
            if now == target:
                return ret
            
            for i in range(N):
                if visited[i]:
                    continue
                
                diff = 0
                for j in range(len(now)):
                    if now[j] != words[i][j]:
                        diff += 1
                
                if diff == 1:
                    visited[i] = True
                    queue.append([words[i], ret+1])

        return 0
    
    ret = bfs()
    
    return ret

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words))