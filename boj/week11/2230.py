import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

end = 0
min_v = 1e11

for start in range(N):
    while end < N and lst[end] - lst[start] < M:
        end += 1
    
    if end == N:
        break

    if lst[end] - lst[start] < min_v:
        min_v = lst[end] - lst[start]

print(min_v)