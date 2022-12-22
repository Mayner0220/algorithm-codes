# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter


def solution(topping: list) -> int:
    answer = 0
    searched = set()
    counter = Counter(topping)

    while len(topping) > 1:
        element = topping.pop()
        searched.add(element)

        if counter[element] > 1:
            counter[element] -= 1
        else:
            del counter[element]

        if len(searched) == len(counter):
            answer += 1
    return answer
