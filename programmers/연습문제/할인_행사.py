# https://school.programmers.co.kr/learn/courses/30/lessons/131127

from collections import Counter


def solution(want: list, number: list, discount: list) -> int:
    answer = 0
    want_dict = {w: n for w, n in zip(want, number)}

    for idx in range(len(discount) - 9):
        if Counter(discount[idx:idx + 10]) == want_dict:
            answer += 1

    return answer
