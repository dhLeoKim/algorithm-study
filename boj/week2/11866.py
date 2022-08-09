from collections import deque

N, K = map(int, input().split())
d = deque(range(1, N+1))

result = []
while len(d) != 0:
    d.rotate(1-K)
    result.append(str(d.popleft()))

print('<' + ', '.join(result) + '>')