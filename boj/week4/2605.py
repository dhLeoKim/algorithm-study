N = int(input())
lst = list(map(int, input().split()))

ret = []
for i in range(len(lst)):
    ret.insert(len(ret)-lst[i], i+1)    # 끝에서 뽑은 수만큼의 앞에 insert

print(*ret)