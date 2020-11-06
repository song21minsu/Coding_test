def solution(board, moves):
    answer = 0
    box=[]

    while moves:
        tmp=moves.pop(0)

        for i in range(len(board)):
            if board[i][tmp-1] != 0:
                box.append(board[i][tmp-1])
                board[i][tmp-1]=0
                if len(box)>1 and box[-1]==box[-2]:
                    answer+=2
                    del box[-2:]
                break

    return answer

board= [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))