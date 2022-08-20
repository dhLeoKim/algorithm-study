C, R = map(int, input().split())
K = int(input())

if K > C*R: print(0)
else:
    move = [1, 0, -1, 0]
    ys = 0
    xs = 4
    while 