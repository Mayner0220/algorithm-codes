# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n: int) -> list:
    matrix = [[0] * n for _ in range(n)]
    answer = []

    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1

            matrix[x][y] = num
            num += 1

    for i in matrix:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer
