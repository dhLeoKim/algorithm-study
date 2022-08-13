# 1
# tree 생성
tree = list(map(lambda x: x//2, range(1024)))

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    # a 조상 정보
    path_a = []
    node_a = a
    while node_a:
        path_a.append(node_a)
        node_a = tree[node_a]

    # b 조상 정보
    path_b = []
    node_b = b
    while node_b:
        path_b.append(node_b)
        node_b = tree[node_b]

    # 가장 가까운 공통 조상 찾기
    for i in path_a:
        if i in path_b: 
            print(i*10)
            break

# 2
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())

    while True:
        if a > b:
            a //= 2
        elif a < b:
            b //= 2
        else:
            print(a*10)
            break