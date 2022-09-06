import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def BFS(J, F):
    QJ = deque()
    QJ.append(J)

    QF = deque()
    QF.append(F)

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    while QJ:
        if QJ: J = QJ.popleft()
        temp = deque()
        while J:
            Ji, Jj = J.popleft()
            for k in range(4):
                Jni = Ji + di[k]
                Jnj = Jj + dj[k]
                if Jni < 0 or Jni > R-1 or Jnj < 0 or Jnj > C-1:
                    if lst[Ji][Jj] != 'F':
                        return lst[Ji][Jj] + 1
                if lst[Ji][Jj] != 'F' and lst[Jni][Jnj] == '.':
                    lst[Jni][Jnj] = lst[Ji][Jj] + 1
                    temp.append((Jni, Jnj))
        if temp:
            QJ.append(temp)

        if QF: F = QF.popleft()
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

J = deque()
F = deque()
for i in range(R):
    for j in range(C):
        if lst[i][j] == 'J':
            J.append((i, j))
            lst[i][j] = 0
        elif lst[i][j] == 'F':
            F.append((i, j))

print(BFS(J, F))

# print(ret)

# for row in lst:
#     print(row)