lst = input()

# {'operator': [icp, isp]} 토큰 우선순위 저장
token = {
    # ')': [],
    '*': [2, 2],
    '/': [2, 2],
    '+': [1, 1],
    '-': [1, 1],
    '(': [3, 0]
}

ret = ''
stack = []
for i in lst:
    if i.isalpha():                             # 피연산자인 경우 후위표기식에 저장
        ret += i
    else:                                       # 연산자인 경우
        if not stack:
            stack.append(i)                     # 빈 stack일 땐 추가
        elif i == ')':
            while stack[-1] != '(':             # ')' 이면 '(' 가 나올 때 까지 pop후 후위표기식에 추가
                ret += stack.pop()
            stack.pop()                         # 괄호는 출력x
        elif token[i][0] > token[stack[-1]][1]: # icp > isp 일 때는 연산자 stack에 쌓기
            stack.append(i)
        else:                                   # icp <= isp 일 때는
            while stack and token[i][0] <= token[stack[-1]][1]: # icp > isp 일때까지 ( '('나올 때 까지) 혹은 stack이 빌때까지
                ret += stack.pop()              # 연산자 pop해서 후위표기식에 추가
            stack.append(i)

while stack:                                    # 마지막으로 stack에 남은 연산자 빼서 추가
    ret += stack.pop()

print(ret)