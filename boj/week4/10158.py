import sys
input = sys.stdin.readline

w, h = map(int, input().split(' '))
p, q = map(int, input().split(' '))
t = int(input())

a, b = divmod(p+t, w)
if a%2: x = w-b
else: x = b

c, d = divmod(q+t, h)
if c%2: y = h-d
else: y = d

print(x, y)

# 예시: x방향 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1 w기준으로 증감 반복
# w로 나눴을 때
# 몫이 짝수면 증가상태이므로 나머지가 x
# 몫이 홀수면 감소상태이므로 w-나머지가 x