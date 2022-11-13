def solution(n, results):
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]

    for w, l in results:
        win[w].append(l)
        lose[l].append(w)

    for i in range(1, n+1):
        for w in win[i]:
            if lose[i]:
                for l in lose[i]:
                    if l not in lose[w]:
                        lose[w].append(l)
                    if w not in win[l]:
                        win[l].append(w)
    
    ret = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            ret += 1

    return ret

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	

print(solution(n, results))