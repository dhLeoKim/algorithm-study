import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from heapq import*

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()  # 주의!!! 왜 시작시간 순서로 정렬해야하는지 생각해보기

room = []
heappush(room, lst[0][1])
for i in range(1, N):
    if lst[i][0] >= room[0]:
        heappop(room)
        heappush(room, lst[i][1])
    else:
        heappush(room, lst[i][1])

print(len(room))

# 주의! 반례
# 4
# 1 2
# 1 4
# 2 6
# 4 5

# 해당 문제는 강의실이 비는 시간을 최소화 해야함!
# 즉 강의가 끝나는 시간과 다음 시작 시간의 차가 작게 최적화