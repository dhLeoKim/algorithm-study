import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

d = [0]*(N+1)
d[0] = [0, 0]
d[1] = [10, 1]

for i in range(1, N+1):
    temp_max = 0
    for j in range(i-1, 0, -1):
        if lst[i-1] > d[j][0]:
            if d[j][1] > temp_max: temp_max = d[j][1]
    d[i] = [lst[i-1], temp_max + 1]

print(max(d, key= lambda x: x[1])[1])