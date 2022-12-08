# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board: list, moves: list) -> int:
    stack = []
    answer = 0

    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] != 0:
                stack.append(board[row][move-1])
                board[row][move-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2
                break

    return answer
