import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    ret = 0
    max_val = lst[-1]
    for i in range(N-1, -1, -1):
        if lst[i] > max_val:
            max_val = lst[i]
        elif lst[i] < max_val:
            ret += max_val - lst[i]
    
    print(ret)