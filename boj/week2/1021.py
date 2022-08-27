from collections import deque

N, M = map(int, input().split())
lst = list(map(int, input().split()))

arr = deque(range(1, N+1))
print(lst, arr)

n = len(arr)
ret = 0
i = arr[-1]
prev = 0
for target in lst:
    target = (target+prev)%n
    # if target > i: target-1
    # i = target

    left = target-1
    right = n+1-target

    if left <= right:
        ret += left
        prev += right-1
    else:
        ret += right
        prev += right-1

    n -= 1
    print(left, right, prev)
    print(ret)