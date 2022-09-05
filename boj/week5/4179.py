import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(Ji, Jj, Fi, Fj):
    QJ = deque()
    J = deque()
    J.append((Ji, Jj))
    QJ.append(J)

    QF = deque()
    F = deque()
    F.append((Fi, Fj))
    QF.append(F)

    # while QJ and QF:
    while True:
        if QJ or QF:
            if QJ: J = QJ.popleft()
            if QF: F = QF.popleft()
        elif not QJ and not QF:
            break

        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]

        temp = deque()
        while J:
            Ji, Jj = J.popleft()
            for k in range(4):
                Jni = Ji + di[k]
                Jnj = Jj + dj[k]
                if Jni < 0 or Jni > R-1 or Jnj < 0 or Jnj > C-1:
                    return lst[Ji][Jj] + 1
                if lst[Ji][Jj] != 'F' and lst[Jni][Jnj] == '.':
                    lst[Jni][Jnj] = lst[Ji][Jj] + 1
                    temp.append((Jni, Jnj))
        if temp:
            QJ.append(temp)

        temp = deque()
        while F:
            Fi, Fj = F.popleft()
            for k in range(4):
                Fni = Fi + di[k]
                Fnj = Fj + dj[k]
                if 0 <= Fni < R and 0 <= Fnj < C and lst[Fni][Fnj] != '#' and lst[Fni][Fnj] != 'F':
                    lst[Fni][Fnj] = 'F'
                    temp.append((Fni, Fnj))
        if temp:
            QF.append(temp)

    return 'IMPOSSIBLE'

R, C = map(int, input().split())
lst = [list(input().strip()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if lst[i][j] == 'J':
            Ji, Jj = i, j
            lst[i][j] = 0
        elif lst[i][j] == 'F':
            Fi, Fj = i, j

print(BFS(Ji, Jj, Fi, Fj))

# print(ret)

# for row in lst:
#     print(row)