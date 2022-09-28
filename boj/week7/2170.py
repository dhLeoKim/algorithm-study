import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

# for i in lst:
#     print(i)

ret = 0
s = lst[0][0]
e = lst[0][1]
for i in lst:
    if i[0] <= e:
        if i[1] > e:
            e = i[1]
    else:
        ret += e-s
        s = i[0]
        e = i[1]

ret += e-s

print(ret)