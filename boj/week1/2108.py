## 아직 풀이 중...

from statistics import mean


N = int(input())

lst = []
for i in range(N):
    lst.append(int(input()))

lst.sort()

lst_mean = sum(lst) / len(lst)
lst_median = lst[len(lst)//2]
cnt = 0
b= set(lst)
for i in b:
    if lst.count(i) > cnt:
        cnt = lst.count(i)
        lst_mode = i

lst_range = max(lst) - min(lst)

print(lst_mean)
print(lst_median)
print(lst_mode)
print(lst_range)