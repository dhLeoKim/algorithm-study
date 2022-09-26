import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

###################
# 시간 초과

# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]

# lst.sort()
# lst.sort(key= lambda x: x[1])

# room = []
# for i in lst:
#     for j in range(len(room)):
#         if i[0] >= room[j][0]:
#             room[j] = [i[1]]
#             break
#     else:
#         room.append([i[1]])

# print(len(room))

from heapq import*

N = int(input())
h = [0]
for _ in range(N):
    s, e = map(int, input().split())
    if s >= h[0]:
        heappop(h)
        heappush(h, e)
    else:
        heappush(h, e)

print(len(h))