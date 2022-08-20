import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = 101
arr = [[0]*N for _ in range(N)]
cnt = 0
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            if arr[i][j] == 0:              # 주어진 영역 1로 채우면서, cnt로 넓이 바로 계산
                arr[i][j] = 1 
                cnt += 1

print(cnt)
# ret = 0
# for i in arr:
#     ret += sum(i)

# print(ret)