# https://school.programmers.co.kr/learn/courses/30/lessons/136798

from math import sqrt
from itertools import chain


def divisors(num: int) -> set:
    return set(chain.from_iterable((i, num // i) for i in range(1, int(sqrt(num)) + 1) if num % i == 0))


def solution(number: int, limit: int, power: int) -> int:
    answer = 0
    for night_num in range(1, number + 1):
        night_power = len(divisors(night_num))
        if night_power > limit:
            answer += power
        else:
            answer += night_power
    return answer
