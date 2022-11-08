def solution(m, n, puddles):
    dp = [[-1]*m for _ in range(n)]
    for j, i in puddles:                # 웅덩이 0으로 표시
        dp[i-1][j-1] = 0

    dp[0][0] = 1

    for j in range(1, m):               # row 초기화
        if dp[0][j]:
            dp[0][j] = dp[0][j-1]

    for i in range(1, n):               # col 초기화
        if dp[i][0]:
            dp[i][0] = dp[i-1][0]

    for i in range(1, n):               # 위, 아래 경우의 수 더해서 dp table 작성
        for j in range(1, m):
            if dp[i][j] == 0:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n-1][m-1] % 1000000007

m, n, puddles = 4, 3, [[2, 2]]
print(solution(m, n, puddles))