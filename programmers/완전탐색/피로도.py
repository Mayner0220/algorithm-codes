# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations


def solution(k: int, dungeons: list) -> int:
    answer = []

    for dungeon in permutations(dungeons):
        fatigue = k
        cnt = 0
        for least, consume in dungeon:
            if fatigue >= least:
                fatigue -= consume
                cnt += 1
            else:
                break
        answer.append(cnt)

    return max(answer)
