# import sys
# sys.stdin = open('test.txt')
# T = int(input())
# for _ in range(T):

#################
# N, K = map(int, input().split())
# num = list(i for i in input())

# for i in range(K):
#     num.remove(min(num[:K]))

# print(f'{"".join(num)}')


##################
N, K = map(int, input().split())
lst = list(i for i in input())
stack = []
cnt = K
idx = 0

while True:
    if cnt == 0: break 
    if idx > len(lst)-1:
        for _ in range(cnt):
            stack.pop()
        break
    if len(stack) == 0: pass
    elif lst[idx] > stack[-1]:
        stack.pop()
        cnt -= 1
        continue
    stack.append(lst[idx])
    idx += 1

for i in range(idx, len(lst)):
    stack.append(lst[i])

print(''.join(stack))