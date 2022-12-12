def solution(word):
    w = []
    lst = ['A', 'E', 'I', 'O', 'U']
    ret, cnt = 0, 0

    def dfs(idx):
        nonlocal cnt, ret
        res = ''.join(w)

        if idx == 5:
            if res == word:
                ret = cnt
            return

        if res == word:
            ret = cnt

        if res < word:               
            for i in range(5):
                cnt += 1
                w.append(lst[i])
                dfs(idx+1)
                w.pop()

    dfs(0)

    return ret

word = "AAAAE"
word = "AAAE"
word = "I"
word = "EIO"

print(solution(word))