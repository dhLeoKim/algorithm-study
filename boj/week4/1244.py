import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst = list(map(bool, lst))
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        change = ([False]*(b-1) + [True])*(N//b) + [False]*(N%b)
        lst = [x ^ y for x, y in zip(lst, change)]

    else:
        k = 1
        while b-1-k >= 0 and b-1+k <= N-1 and lst[b-1-k] == lst[b-1+k]:
            k += 1
        k -= 1
        change = [False]*(b-1-k) + [True]*(2*k+1) + [False]*(N-b-k)
        lst = [x ^ y for x, y in zip(lst, change)]

lst = list(map(int, lst))
for i in range(len(lst)):
    print(lst[i], end=' ')
    if i%20 == 19: print()