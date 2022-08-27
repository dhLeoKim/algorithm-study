import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst = list(map(bool, lst))
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:                                                          # 남학생
        change = ([False]*(b-1) + [True])*(N//b) + [False]*(N%b)        # 배수의 인덱스에서만 1인 배열 생성
        lst = [x ^ y for x, y in zip(lst, change)]                      # xor 연산으로 스위칭

    else:                                                               # 여학생
        k = 1
        while b-1-k >= 0 and b-1+k <= N-1 and lst[b-1-k] == lst[b-1+k]:
            k += 1
        k -= 1
        change = [False]*(b-1-k) + [True]*(2*k+1) + [False]*(N-b-k)     # 대칭인 인덱스까지만 1인 배열 생성
        lst = [x ^ y for x, y in zip(lst, change)]                      # xor 연산

lst = list(map(int, lst))
for i in range(len(lst)):
    print(lst[i], end=' ')                                              # 20칸씩 출력하기
    if i%20 == 19: print()