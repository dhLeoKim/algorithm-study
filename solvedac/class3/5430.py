import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

T = int(input())
for case in range(T):
    p = input().strip()
    n = int(input())
    deq = deque(input().strip()[1:-1].split(','))

    flag = True
    for cmd in p:
        if cmd == 'D':
            n -= 1
            if n < 0: 
                print('error')
                break
            if flag:
                deq.popleft()
            else:
                deq.pop()
        elif cmd == 'R':
            flag = not flag

    else:
        if flag:
            print('[' + ','.join(deq) + ']')
        else:
            deq.reverse()
            print('[' + ','.join(deq) + ']')