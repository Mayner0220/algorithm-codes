# https://school.programmers.co.kr/learn/courses/30/lessons/135807

from math import gcd
from functools import reduce


def solution(arrayA: list, arrayB: list) -> int:
    gcd_a, gcd_b = int(reduce(gcd, arrayA)), int(reduce(gcd, arrayB))
    answer = 0

    if all(num % gcd_b for num in arrayA):
        answer = max(answer, gcd_b)

    if all(num % gcd_a for num in arrayB):
        answer = max(answer, gcd_a)

    return answer
