def solution(brown, yellow):
    N = (brown-4) // 2
    for i in range(N):
        if i*(N-i) == yellow:
            w, h = i+2, N-i+2
            break

    return [h, w]

brown, yellow = 10, 2
# brown, yellow = 8, 1
# brown, yellow = 24, 24

print(solution(brown, yellow))