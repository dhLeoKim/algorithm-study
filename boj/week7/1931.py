import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()
lst.sort(key= lambda x: x[1])

end = 0
ret = 0
for i in lst:
    if i[0] >= end:
        ret += 1
        end = i[1]

print(ret)