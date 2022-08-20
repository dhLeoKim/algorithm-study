import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = 9
lst = [int(input()) for _ in range(N)]

for i in range(1<<N):                           # 비트 연산자로 부분 집합 생성
    temp = []
    for j in range(N):
        if i & (1<<j):
            temp.append(lst[j])
    
    if len(temp) == 7 and sum(temp) == 100:     # 난쟁이 조건을 만족하면 출력
        print('\n'.join(map(str, sorted(temp))))
        break
        # 가능 한 경우의 수가 많으니 break 꼭꼭!!!