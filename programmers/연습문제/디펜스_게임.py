# https://school.programmers.co.kr/learn/courses/30/lessons/142085

import heapq


def solution(n: int, k: int, enemy: list) -> int:
    heap = []
    total = 0

    for round_cnt, enemy_num in enumerate(enemy, start=1):
        total += enemy_num
        if total <= n:
            heapq.heappush(heap, -enemy_num)
        elif k > 0:
            k -= 1
            total += heapq.heappushpop(heap, -enemy_num)
        else:
            return round_cnt - 1
    return round_cnt
