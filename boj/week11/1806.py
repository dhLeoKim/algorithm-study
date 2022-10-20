import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def func():
    end = 0
    subtotal = lst[0]
    min_l = 1e11

    for start in range(N):
        while subtotal < S and end < N:
            end += 1
            if end == N:
                return min_l
            subtotal += lst[end]

        l = end - start + 1
        if l < min_l:
            min_l = l

        subtotal -= lst[start]

    return min_l

N, S = map(int, input().split())
lst = list(map(int, input().split()))

ret = func()
print(0 if ret == 1e11 else ret)