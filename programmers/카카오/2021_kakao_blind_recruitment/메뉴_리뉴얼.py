# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for combination_num in course:
        menu_combination = []
        for order in orders:
            order = sorted(order)
            menu_combination.extend(list(combinations(order, combination_num)))

        combination_count = Counter(menu_combination)

        if combination_count:
            if max(combination_count.values()) >= 2:
                for key, value in combination_count.items():
                    if value == max(combination_count.values()):
                        answer.append("".join(key))

    return sorted(answer)
