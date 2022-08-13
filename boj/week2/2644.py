# import sys
# sys.stdin = open('input_2644.txt')

# T = int(input())
# for case in range(T):

n = int(input())
a, b = map(int, input().split())
m = int(input())

tree = [0]*(n+1)

# tree에서 부모의 정보를 저장
for _ in range(m):
    x, y = map(int, input().split())
    tree[y] = x

ancestor_a = []
ancestor_b = []

# a의 조상을 list로 저장
node_a = a
while node_a:
    ancestor_a.append(node_a)
    node_a = tree[node_a]

# b의 조상을 list로 저장
node_b = b
while node_b:
    ancestor_b.append(node_b)
    node_b = tree[node_b]

# a와 b의 공통 조상을 찾고
for i in ancestor_a:
    if i in ancestor_b:
        # 공통 조상이 있으면 촌수를 출력
        print(ancestor_a.index(i) + ancestor_b.index(i))
        break
# 없으면 -1 출력
else:
    print(-1)