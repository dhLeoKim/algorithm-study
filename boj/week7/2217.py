N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort(reverse=True)

ret = []
for i in range(len(lst)):
    temp = lst[i]*(i+1)
    ret.append(temp)

print(max(ret))