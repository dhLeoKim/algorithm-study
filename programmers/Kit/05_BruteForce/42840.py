def solution(answers):
    ret = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, ans in enumerate(answers):
        if ans == one[idx % 5]:
            ret[0] += 1
        if ans == two[idx % 8]:
            ret[1] += 1
        if ans == thr[idx % 10]:
            ret[2] += 1
    
    print(ret)

    res = []
    for idx, sco in enumerate(ret):
        if sco == max(ret):
            res.append(idx+1)

    return res

answers = [1,2,3,4,5]	
# answers = [1,3,2,4,2]

print(solution(answers))