import sys
sys.stdin = open('input_15868.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
home = []
chicken = []
lst = []
for i in range(N):
    row = list(map(int, input().split()))
    lst.append(row)
    for j in range(N):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))


from itertools import combinations

chicken_lst = list(combinations(list(range(len(chicken))), M))      # 치킨집 선택하는 조합

H = len(home)
ret = 1e9

# 도시의 치킨거리 계산
def calc(idx, dist, case):
    global ret

    if idx == H:                                        # 모든 집 다 계산 후, 최소값 업데이트
        if dist < ret:
            ret = dist
        return
    
    if dist + H - idx >= ret:                           # 가지치기
        return

    tmp = 1e9
    hi, hj = home[idx]
    for k in case:
        ci, cj = chicken[k]

        tmp = min(tmp, abs(ci-hi) + abs(cj-hj))         # 해당 집의 치킨거리 계산

    calc(idx+1, dist+tmp, case)

for case in chicken_lst:                                # 모든 경우의 수에 대해 치킨거리 계산
    calc(0, 0, case)

print(ret)