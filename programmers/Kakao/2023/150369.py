def solution(cap, n, deliveries, pickups):
    ret = 0
    cap_d = cap_p = cap                         # 배달/수거할 때 cap
    flag_d = flag_p = False                     # 첫번째 배달/수거 확인용 flag
    chk = [0]*n*50                              # 돌아가는 포인트를 저장, 최대 경우의 수 n*50
    di = pi = 0                                 # 돌아가는 포인트 확인용 index

    for i in range(n-1, -1, -1):
        # 첫번째 배달/수거 확인 후, chk 저장
        if not flag_d and deliveries[i] != 0:
            flag_d = True
            chk[di] = max(chk[di], i+1)
            di += 1
        if not flag_p and pickups[i] != 0:
            flag_p = True
            chk[pi] = max(chk[pi], i+1)
            pi += 1

        # i 에서의 배달/수거 cap
        cap_d -= deliveries[i]
        cap_p -= pickups[i]

        # 배달/수거 진행, 같은 턴(?)의 돌아가는 포인트 중 더 먼값만 chk에 저장
        while cap_d < 0:
            cap_d += cap
            chk[di] = max(chk[di], i+1)
            di += 1
        while cap_p < 0:
            cap_p += cap
            chk[pi] = max(chk[pi], i+1)
            pi += 1

    ret = sum(chk)*2

    return ret

cap = 4	
n = 5	
deliveries = [1, 0, 3, 1, 2]	
pickups = [0, 3, 0, 4, 0]	
# 16 (5+5+3+3)

# cap = 2	
# n = 7	
# deliveries = [1, 0, 2, 0, 1, 0, 2]	
# pickups = [0, 2, 0, 1, 0, 2, 0]	
# # 30 (7+7+5+5+3+3)

# print(solution(cap, n, deliveries, pickups))
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]), 16)
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]), 30)
print(solution(4, 5, [8, 0, 8, 0, 4], [0, 0, 0, 0, 20]), 50)
print(solution(2, 2, [0, 1], [0, 4]), 8)
print(solution(2, 2, [0, 0], [0, 6]), 12)
print(solution(2, 2, [0, 0], [4, 0]), 4)
print(solution(2, 2, [5, 0], [0, 3]), 10)
print(solution(5, 3, [5, 0, 5], [0, 1, 10]), 16)
print(solution(5, 3, [5, 1, 5], [0, 1, 10]), 16)
print(solution(2, 3, [0, 6, 13], [19, 0, 1]), 54)
print(solution(2, 3, [4, 2, 1], [0, 4, 1]), 16)
print(solution(4, 5, [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 12)
print(solution(4, 4, [25, 24, 51, 0], [51, 0, 0, 49]), (13 * 4 + 6 * 2 + 6) * 2)