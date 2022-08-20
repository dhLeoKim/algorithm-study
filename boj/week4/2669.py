import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
N = 101
arr = [[0]*N for _ in range(N)]

T = 4
for _ in range(T):
    lst = list(map(int, input().split()))

    for i in range(lst[0], lst[2]):             # 주어진 범위를 1로 채우기
        for j in range(lst[1], lst[3]):
            arr[i][j] = 1

ret = 0
for i in arr:           # 1 모두 더해서 영역 구하기
    ret += sum(i)
print(ret)