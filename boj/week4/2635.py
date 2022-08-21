# n = int(input())

# ret = []
# max_cnt = 0
# for i in range(1, n+1):
#     lst = [n, i]
#     cnt = 2
#     nxt = 0
#     while nxt >= 0:
#         nxt = lst[-2] - lst[-1]
#         lst.append(nxt)
#     lst.pop()    
#     if len(lst) > max_cnt:
#         max_cnt = len(lst)
#         ret = lst

# print(max_cnt)
# print(*ret)


# 이게 더 빠른듯?
n = int(input())

max_cnt = 0
for i in range(1, n+1):
    lst = [n, i]                        # d[0], d[1] 초기값 설정
    cnt = 2
    while True:
        nxt = lst[-2] - lst[-1]         # d[i] = d[i-1] - d[i-2]
        if nxt >= 0:
            lst.append(nxt)
            cnt += 1
        else:                           # 음수가 나올 때 까지
            break
    if cnt > max_cnt:
        max_cnt = cnt
        ret = lst

print(max_cnt)
print(*ret)