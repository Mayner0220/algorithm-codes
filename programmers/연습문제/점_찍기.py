# https://school.programmers.co.kr/learn/courses/30/lessons/140107

from math import sqrt


def solution(k: int, d: int) -> int:
    answer = 0

    for x in range(0, d + 1, k):
        max_y = int(sqrt(d ** 2 - x ** 2))
        answer += int(max_y / k + 1)
    return answer
