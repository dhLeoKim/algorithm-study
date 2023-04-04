import sys
sys.stdin = open('input_12100.txt')
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

def calcLine(line):
    line_nxt = []
    prev = 0
    for i in range(N):
        if prev == 0:                                       # prev 업데이트
            prev = line[i]
        elif line[i] == 0:                                  # 0인 경우 다음으로
            continue
        elif line[i] == prev:                               # 같으면 2배 후 추가
            line_nxt.append(prev*2)
            prev = 0
        else:                                               # 다르면 추가
            line_nxt.append(prev)
            prev = line[i]

    if prev != 0:                                           # 남은 블록 추가
        line_nxt.append(prev)

    line_nxt += [0]*(N-len(line_nxt))                       # 나머지 0 추가

    return line_nxt


def calc(lst, direction):
    lst_nxt = []

    # 0 : 상, 1 : 우, 2 : 하, 3 : 좌
    if direction == 0:                                      # 위쪽으로
        for line in zip(*lst):                              # col으로 계산후 Transpose
            lst_nxt.append(calcLine(line))
        lst_nxt = list(map(list, zip(*lst_nxt)))            

    elif direction == 1:                                    # 오른쪽으로
        for line in lst:
            lst_nxt.append(calcLine(line[::-1])[::-1])

    elif direction == 2:                                    # 아래쪽으로
        for line in zip(*lst):                              # col으로 계산후 Transpose
            lst_nxt.append(calcLine(line[::-1])[::-1])
        lst_nxt = list(map(list, zip(*lst_nxt)))

    else:                                                   # 왼쪽으로
        for line in lst:
            lst_nxt.append(calcLine(line))

    return lst_nxt


def dfs(depth, lst):
    global ret
    if depth == 5:
        tmp = []
        for row in lst:
            tmp.append(max(row))
        ret = max(ret, max(tmp))            # 최대값 갱신
        return
    
    for direction in range(4):              # 방향 선택 경우의 수 생성
        lst_nxt = calc(lst, direction)

        dfs(depth+1, lst_nxt)


ret = 0
dfs(0, lst)

print(ret)