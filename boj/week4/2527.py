import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    dx = max(x1, x2) - min(p1, p2)
    dy = max(y1, y2) - min(q1, q2)
    
    # 경우의 수 정리
    # d : max(x1, x2) > min(p1, p2) or max(y1, y2) > min(q1, q2)
    # a : max(x1, x2) < min(p1, p2) and max(y1, y2) < min(q1, q2)
    # c : max(x1, x2) == min(p1, p2) and max(y1, y2) == min(q1, q2)
    # b : max(x1, x2) < min(p1, p2) and max(y1, y2) == min(q1, q2)
    #   : or
    #   : max(x1, x2) == min(p1, p2) and max(y1, y2) < min(q1, q2)

    if dx > 0 or dy > 0:
        print('d')
    elif dx < 0 and dy < 0:
        print('a')
    elif dx == 0 and dy == 0:
        print('c')
    else:
        print('b')