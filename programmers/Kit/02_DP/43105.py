def solution(triangle):
    N = len(triangle)
    dp = [[] for _ in range(N)]
    dp[-1] = triangle[-1]               # 초기값
    
    for i in range(N-2, -1, -1):        # 아래에서 부터 쌓아가기
        for j in range(i+1):            
            dp[i].append(max(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j])
    
    return dp[0][0]

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))