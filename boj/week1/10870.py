N = int(input())

fib = [0, 1]
for i in range(N):
    fib[0], fib[1] = fib[1], fib[0] + fib[1]

print(fib[0])