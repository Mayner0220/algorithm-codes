# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter


def solution(k: int, tangerine: list) -> int:
    answer = 0

    for cnt in [cnt for _, cnt in Counter(tangerine).most_common()]:
        if k <= 0:
            break
        answer += 1
        k -= cnt
    return answer
