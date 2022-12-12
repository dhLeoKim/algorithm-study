from itertools import permutations

def solution(numbers):
    temp = []
    for i in range(1, len(numbers)+1):
        temp += list(permutations(numbers, i))
    
    temp = [int(("").join(p)) for p in temp]
    temp = list(set(temp))
    
    ret = 0
    for num in temp:                        
        if num >= 2:                                
            flag = True            
            for j in range(2, num):       
                if num % j == 0:                       
                    flag = False
                    break
            if flag:
                ret += 1

    return ret


numbers = '17'
# numbers = '011'

print(solution(numbers))