import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, k = map(int, input().split())
lst = [[0]*6, [0]*6]                    # lst[성별][학년] 초기화
cnt = 0
for _ in range(N):
    S, Y = map(int, input().split())
    lst[S][Y-1] += 1

for i in lst:
    for j in i:
        a, b = divmod(j, k)             # 몫 + 나머지가 존재하면 +1
        cnt += a + bool(b)

print(cnt)