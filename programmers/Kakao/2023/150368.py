def solution(users, emoticons):
    
    N = len(users)
    M = len(emoticons)
    dc = [10, 20, 30, 40]
    lst = []
    ret = [0, 0]

    def dfs(idx):
        nonlocal ret
        if idx == M:
            # 해당 경우의 수에서, [서비스가입수, 판매가] 계산
            tmp = [0 , [0]*N]
            for j in range(N):
                for k in range(M):
                    if users[j][0] <= lst[k][0]:
                        tmp[1][j] += lst[k][1]
                
                if tmp[1][j] >= users[j][1]:
                    tmp[0] += 1
                    tmp[1][j] = 0

            # 목표에 부합하는지 비교
            tmp[1] = sum(tmp[1])
            if tmp[0] >= ret[0] and tmp[1] > ret[1]:
                ret = tmp
            elif tmp[0] > ret[0]:
                ret = tmp
            return 
        
        # 중복조합 생성, [할인율, 구매가] 로 저장
        for i in range(4):
            lst.append([dc[i], int(emoticons[idx]*(100-dc[i])/100)])
            dfs(idx+1)
            lst.pop()

    dfs(0)

    return ret

users = [[40, 10000], [25, 10000]]	
emoticons = [7000, 9000]	
#[1, 5400]

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]	
emoticons = [1300, 1500, 1600, 4900]	
# [4, 13860]

print(solution(users, emoticons))