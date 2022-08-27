import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().strip()

    stack = []
    result = ''
    for i in s:
        if i == ' ':
            while stack:
                result += stack.pop()
            result += i
        else:
            stack.append(i)

    while stack:
        result += stack.pop()

    print(result)