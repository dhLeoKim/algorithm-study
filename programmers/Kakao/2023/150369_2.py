def solution(cap, n, deliveries, pickups):
    ret = 0
    d = 0
    p = 0
    
    for i in range(n-1, -1, -1):
        # 택배/수거 할 숫자
        d += deliveries[i]
        p += pickups[i]
        
        # 양수면 돌아가는 가장 먼 지점
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            ret += (i+1)*2

    return ret

cap = 4	
n = 5	
deliveries = [1, 0, 3, 1, 2]	
pickups = [0, 3, 0, 4, 0]	
# 16

# cap = 2	
# n = 7	
# deliveries = [1, 0, 2, 0, 1, 0, 2]	
# pickups = [0, 2, 0, 1, 0, 2, 0]	
# # 30

print(solution(cap, n, deliveries, pickups))