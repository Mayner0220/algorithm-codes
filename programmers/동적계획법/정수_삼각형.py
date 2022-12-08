# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle: list) -> int:
    for row in range(1, len(triangle)):
        for col in range(row+1):
            if col == 0:
                triangle[row][col] += triangle[row-1][col]
            elif row == col:
                triangle[row][col] += triangle[row-1][col-1]
            else:
                triangle[row][col] += max(triangle[row-1][col], triangle[row-1][col-1])
    return max(triangle[-1])
