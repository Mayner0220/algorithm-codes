# https://school.programmers.co.kr/learn/courses/30/lessons/150368

from math import ceil
from itertools import product


def solution(users: list, emoticons: list) -> list:
    min_discount = 100
    max_discount = 0
    answer = [0, 0]

    for (user_discount, _) in users:
        min_discount = min(min_discount, ceil(user_discount / 10) * 10)
        max_discount = max(max_discount, ceil(user_discount / 10) * 10)

    min_to_max = [discount_rate for discount_rate in range(min_discount, max_discount + 10, 10)]
    permutations = list(product(*[min_to_max for _ in range(len(emoticons))]))

    for permutation in permutations:
        service_cnt, total_price = 0, 0
        for (user_discount, criteria_price) in users:
            price = 0
            for emoticon, p in zip(emoticons, permutation):
                if p >= user_discount:
                    price += emoticon * (100 - p) / 100
            if price >= criteria_price:
                service_cnt += 1
            else:
                total_price += int(price)

        answer = max(answer, [service_cnt, total_price])

    return answer
