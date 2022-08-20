import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

M, N = map(int, input().split())
grid = [[0]*M for _ in range(N)]
lst = [[], []]                      
n = int(input())
for _ in range(n):                      # lst[가로, 세로 구분][점선 번호]
    a, b = map(int, input().split())
    lst[a].append(b)

lst[0].sort()
lst[0].append(N)                        # 정렬 후 N 추가
lst[1].sort()
lst[1].append(M)                        # 정렬 후 M 추가
row = []
col = []
s = 0
for i in lst[0]:                        # 세로 길이 구분 (가로 자르기)
    col.append(i-s)
    s = i
s = 0
for i in lst[1]:                        # 가로 길이 구분 (세로 자르기)
    row.append(i-s)
    s = i

print(max(row) * max(col))              # max면적