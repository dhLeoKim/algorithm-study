def solution(sizes):
    width = []
    height = []

    for w, h in sizes:
        if w < h:
            w, h = h, w

        width.append(w)
        height.append(h)    

    return max(width)*max(height)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution(sizes))