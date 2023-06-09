import sys
input=sys.stdin.readline

def board_move(board, direction):
    N = len(board)
    new_board = [[board[i][j] for j in range(N)] for i in range(N)]
    
    if direction == 'left':
        for i in range(N):
            current_index = 0
            joined = False
            for j in range(N):
                if board[i][j] == 0:
                    continue
                if joined:
                    joined = False
                    continue
                if j == N - 1:
                    new_board[i][current_index] = board[i][j]
                else:
                    for k in range(j + 1, N):
                        if board[i][k] != 0:
                            break
                    if board[i][j] == board[i][k]:
                        new_board[i][current_index] = 2 * board[i][j]
                        joined = True
                    else:
                        new_board[i][current_index] = board[i][j]
                current_index += 1
            for j in range(current_index, N):
                new_board[i][j] = 0
                
    elif direction == 'right':
        for i in range(N):
            current_index = N - 1
            joined = False
            for j in reversed(range(N)):
                if board[i][j] == 0:
                    continue
                if joined:
                    joined = False
                    continue
                if j == 0:
                    new_board[i][current_index] = board[i][j]
                else:
                    for k in reversed(range(j)):
                        if board[i][k] != 0:
                            break
                    if board[i][j] == board[i][k]:
                        new_board[i][current_index] = 2 * board[i][j]
                        joined = True
                    else:
                        new_board[i][current_index] = board[i][j]
                current_index -= 1
            for j in range(0, current_index + 1):
                new_board[i][j] = 0
                
    elif direction == 'up':
        for j in range(N):
            current_index = 0
            joined = False
            for i in range(N):
                if board[i][j] == 0:
                    continue
                if joined:
                    joined = False
                    continue
                if i == N - 1:
                    new_board[current_index][j] = board[i][j]
                else:
                    for k in range(i + 1, N):
                        if board[k][j] != 0:
                            break
                    if board[k][j] == board[i][j]:
                        new_board[current_index][j] = 2 * board[i][j]
                        joined = True
                    else:
                        new_board[current_index][j] = board[i][j]
                current_index += 1
            for i in range(current_index, N):
                new_board[i][j] = 0
                
    elif direction == 'down':
        for j in range(N):
            current_index = N - 1
            joined = False
            for i in reversed(range(N)):
                if board[i][j] == 0:
                    continue
                if joined:
                    joined = False
                    continue
                if i == 0:
                    new_board[current_index][j] = board[i][j]
                else:
                    for k in reversed(range(i)):
                        if board[k][j] != 0:
                            break
                    if board[k][j] == board[i][j]:
                        new_board[current_index][j] = 2 * board[i][j]
                        joined = True
                    else:
                        new_board[current_index][j] = board[i][j]
                current_index -= 1
            for i in range(0, current_index + 1):
                new_board[i][j] = 0
    
    return new_board

def dfs(depth, board):
    N = len(board)
    if depth == 0:
        return max([board[i][j] for i in range(N) for j in range(N)])
    res = 0
    for direction in ['up', 'down', 'left', 'right']:
        res = max(res, dfs(depth - 1, board_move(board, direction)))
    return res

if __name__ == '__main__':
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int,input().split())))
    print(dfs(5, board))