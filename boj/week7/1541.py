import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

lst = list(input().strip())
lst.append('+')

ret = 0
flag = False
num = ''
for i in lst:
    if i.isdigit():
        num += i
    else:
        if flag:
            ret -= int(num)
            num = ''
            continue
        else:
            ret += int(num)
            num = ''

        if i == '-':
            flag = True

print(ret)