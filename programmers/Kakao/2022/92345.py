from collections import deque

def solution(board, aloc, bloc):
    N = len(board) # 세로길이
    M = len(board[0]) # 가로길이
    
    print(N, M)

    def play():
        return

    loc = deque()
    loc.append(aloc)
    loc.append(bloc)

    def play(board, loc):
        if len(loc) == 1:
            return

        i, j = loc.popleft()
        di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < M and board[ni][nj]:
                loc.append([ni, nj])
                # 재귀로 넘기기
                board[i][j] = 0
                play(board, loc)
                loc.popleft()
                board[i][j] = 1
        
        return

    return

board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]	
aloc = [1, 0]	
bloc = [1, 2]	

# board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]	
# aloc = [1, 0]	
# bloc = [1, 2]	

# board = [[1, 1, 1, 1, 1]]	
# aloc = [0, 0]	
# bloc = [0, 4]	

board = [[1]]	
aloc = [0, 0]	
bloc = [0, 0]	

print(solution(board, aloc, bloc))