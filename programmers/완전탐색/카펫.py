# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown: int, yellow: int) -> list:
    carpet = brown+yellow

    for col in range(carpet, 2, -1):
        if carpet % col == 0:
            row = carpet//col
            if yellow == (col-2)*(row-2):
                return [col, row]
