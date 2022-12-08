# https://school.programmers.co.kr/learn/courses/30/lessons/42576

import collections as col


def solution(participant: list, completion: list) -> str:
    return list((col.Counter(participant) - col.Counter(completion)).keys())[0]
