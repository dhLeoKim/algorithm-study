import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()
lst.sort(key= lambda x: x[1])

# 시간 초과
room = []
for i in lst:
    for j in range(len(room)):
        if i[0] >= room[j][0]:
            room[j] = [i[1]]
            break
    else:
        room.append([i[1]])

print(len(room))