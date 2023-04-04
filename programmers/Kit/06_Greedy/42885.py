def solution(people, limit):
    people.sort()
    start = 0
    end = len(people) - 1
    cnt = 0
    
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else: end -= 1
        cnt += 1
    
    return cnt    

people = [70, 50, 80, 50]
limit = 100

people = [70, 80, 50]
limit = 100

print(solution(people, limit))