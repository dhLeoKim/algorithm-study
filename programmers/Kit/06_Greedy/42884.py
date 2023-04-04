def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    location = -30001
    
    for start, end in routes:
        if start <= location:
            continue
        location = end
        answer += 1
        
    return answer


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

print(solution(routes))