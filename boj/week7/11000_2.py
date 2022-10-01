import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# heap사용 안한 코드

n = int(input())
start = []
finish = []
for _ in range(n):
    s, t = map(int, input().split())
    start.append(s)
    finish.append(t)
start.sort()
finish.sort()

answer = 0
dup = 0
f_idx = 0
for s in start:
    dup += 1
    while finish[f_idx] <= s:
        dup -= 1
        f_idx += 1
    answer = max(answer, dup)
print(answer)