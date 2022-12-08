# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows: int, columns: int, queries: list) -> list:
    answer = []
    matrix = [[0 for _ in range(columns+1)] for _ in range(rows+1)]

    cnt = 1
    for R in range(1, rows+1):
        for C in range(1, columns+1):
            matrix[R][C] = cnt
            cnt += 1

    for x1, y1, x2, y2 in queries:
        last_val = matrix[x1][y1]
        min_val = last_val

        for x in range(x1, x2):
            matrix[x][y1] = matrix[x+1][y1]
            min_val = min(min_val, matrix[x][y1])
        for y in range(y1, y2):
            matrix[x2][y] = matrix[x2][y+1]
            min_val = min(min_val, matrix[x2][y])
        for x in range(x2, x1, -1):
            matrix[x][y2] = matrix[x-1][y2]
            min_val = min(min_val, matrix[x][y2])
        for y in range(y2, y1, -1):
            matrix[x1][y] = matrix[x1][y-1]
            min_val = min(min_val, matrix[x1][y])

        matrix[x1][y1+1] = last_val
        answer.append(min_val)

    return answer
