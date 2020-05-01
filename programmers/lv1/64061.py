# https://programmers.co.kr/learn/courses/30/lessons/64061
# 2019 카카오 개발자 겨울 인턴십
# 크레인 인형뽑기 게임

def solution(board, moves):
    basket = []
    answer = 0
    for move in moves:
        move = move - 1
        doll = 0

        for i in range(len(board)):
            if board[i][move] != 0:
                doll = board[i][move]
                board[i][move] = 0
                break

        if basket[-1:] == [doll] and doll != 0:
            basket.pop()
            answer += 2
        else:
            basket.append(doll)

    return answer