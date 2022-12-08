# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n: int, lost: list, reserve: list) -> int:
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for index in set_reserve:
        if index - 1 in set_lost:
            set_lost.remove(index - 1)
        elif index + 1 in set_lost:
            set_lost.remove(index + 1)

    return n - len(set_lost)
