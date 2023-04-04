def solution(n, lost, reserve):
    reserves = set(reserve) - set(lost)
    losts = set(lost) - set(reserve)

    for now in reserves:
        front = now - 1
        back = now + 1

        if front in losts:
            losts.remove(front)
        elif back in losts:
            losts.remove(back)

    return n - len(losts)

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

# n = 5
# lost = [2, 4]
# reserve = [3]

# n = 3
# lost = [3]
# reserve = [1]

print(solution(n, lost, reserve))