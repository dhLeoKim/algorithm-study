N = int(input())
lst = input()
num = []
for _ in range(N):
    num.append(int(input()))

stack = []

for i in lst:
    if i.isalpha():
        idx = ord(i)-65
        stack.append(num[idx])
    else:
        b = stack.pop()
        a = stack.pop()
        
        if i == '+': stack.append(a + b)
        elif i == '-': stack.append(a - b)
        elif i == '*': stack.append(a * b)
        elif i == '/': stack.append(a / b)
print(f'{stack[0]:.2f}')