def solution(board, moves):
    answer = 0
    tmp = []
    for k in moves:
        for i in range(len(board)):
            if board[i][k - 1]:
                if tmp:
                    if tmp[-1] == board[i][k - 1]:
                        tmp.pop()
                        board[i][k - 1] = 0
                        answer += 1
                    else:
                        tmp.append(board[i][k - 1])
                        board[i][k - 1] = 0
                else:
                    tmp.append(board[i][k - 1])
                    board[i][k - 1] = 0
                break

    return answer * 2

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))