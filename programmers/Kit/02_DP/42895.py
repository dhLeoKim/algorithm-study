def solution(N, number):
    dp = []                             # 사용한 숫자의 횟수를 index로 하는 dp table 작성
    for _ in range(9):
        dp_set = set()                  # 빈 set 사용시에는 set() 으로 작성, {} 는 dict 취급
        dp.append(dp_set)

    for i in range(1, 9):
        dp[i].add(int(str(N)*i))        # NNN 과 같은 경우

        for j in range(1, i):
            for x in dp[j]:             # i 번 사용하는 숫자는
                for y in dp[i-j]:       # (j 번 사용한 숫자, i-j 번 사용한 숫자)의 조합
                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y != 0:
                        dp[i].add(x//y)
    
        if number in dp[i]:
            return i

    return -1

N, number = 5, 12
N, number = 2, 11

print(solution(N, number))