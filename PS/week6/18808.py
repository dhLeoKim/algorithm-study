import sys
sys.stdin = open('input_18808.txt')
input = sys.stdin.readline

def chk(si, sj):
    global SI, SJ
    # 시작점부터 스티커 붙일 수 있는지 확인
    for i in range(R):
        for j in range(C):
            if laptop[si+i][sj+j] == 1 and sticker[i][j] == 1:
                return False

    SI, SJ = si, sj
    return True


def chkSticker():
    # 스티커 붙일 시작점 확인
    for si in range(N-R+1):
        for sj in range(M-C+1):
            if chk(si, sj):
                return True
            
    return False

    
N, M, K = map(int, input().split())
laptop = [[0]*M for _ in range(N)]
stickers = []
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for i in range(R)]
    stickers.append([R, C, sticker])

for tmp in stickers:
    R, C, sticker = tmp

    # 회전하면서 확인
    for cw in range(4):
        SI, SJ = 0, 0

        # 범위 안에 있고, 스티커 붙일 수 있는지 확인
        if R <= N and C <= M and chkSticker():
            # 스티커 붙이기
            for i in range(R):
                for j in range(C):
                    if laptop[SI+i][SJ+j] == 0 and sticker[i][j] == 1:
                        laptop[SI+i][SJ+j] = 1
            break

        # 회전
        R, C = C, R        
        # 시계방향 90도 회전
        sticker = list(map(list, zip(*sticker[::-1])))

        # # 반시계방향 90도 회전
        # sticker_CCW = list(map(list, zip(*sticker)))[::-1]

ret = 0
for row in laptop:
    ret += sum(row)

print(ret)