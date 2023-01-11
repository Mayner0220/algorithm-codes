# https://school.programmers.co.kr/learn/courses/30/lessons/64064

import re

from itertools import permutations


def solution(user_id: list, banned_id: list) -> int:
    ban_candidate = set()
    banned_id = [banned.replace("*", ".") for banned in banned_id]

    for user in permutations(user_id, len(banned_id)):
        if all(re.match(b, u) and len(b) == len(u) for (b, u) in zip(banned_id, user)):
            ban_candidate.add(tuple(sorted(user)))

    return len(ban_candidate)
