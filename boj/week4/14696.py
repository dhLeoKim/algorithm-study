import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    cnt = [0]*5                 # 숫자를 count 하는 배열

    lst1 = list(map(int, input().split()))
    a = lst1[1:]
    for i in a:                 # A의 딱지 숫자에 해당하는 cnt배열 ++
        cnt[i] += 1
    
    lst2 = list(map(int, input().split()))
    b = lst2[1:]
    for i in b:                 # B의 딱지 숫자에 해당하는 cnt 배열 --
        cnt[i] -= 1

    for i in range(4, 0, -1):   # cnt 배열을 뒤에서부터 읽으면서
        if cnt[i] > 0:          # 양수이면 A가 승리
            print('A')
            break
        elif cnt[i] < 0:        # 음수이면 B가 승리
            print('B')
            break
    else:
        print('D')