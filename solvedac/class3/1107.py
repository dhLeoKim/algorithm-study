import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = list(map(int, input().split()))

cnt = abs(100 - N)

for num in range(1000001):
    num_str = str(num)
    n = len(num_str)

    for i in range(n):
        if int(num_str[i]) in lst:
            break
        
        elif i == n - 1:
            cnt = min(cnt, abs(num - N) + n)

print(cnt)