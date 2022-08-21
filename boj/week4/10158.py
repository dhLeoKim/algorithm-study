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