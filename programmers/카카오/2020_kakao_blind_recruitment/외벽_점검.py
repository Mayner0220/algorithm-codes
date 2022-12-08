# https://school.programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations


def solution(n: int, weak: list, dist: list) -> int:
    weak_length = len(weak)

    for idx in range(weak_length):
        weak.append(weak[idx] + n)

    answer = len(dist) + 1

    for idx in range(weak_length):
        start_point = [weak[Check] for Check in range(idx, idx + weak_length)]

        candidates = permutations(dist, len(dist))

        for Order in candidates:
            friend_idx = 0
            friend_count = 1
            possible_check_length = start_point[0] + Order[friend_idx]

            for Idx in range(weak_length):
                if start_point[Idx] > possible_check_length:
                    friend_count += 1

                    if friend_count > len(Order):
                        break

                    friend_idx += 1
                    possible_check_length = Order[friend_idx] + start_point[Idx]

            answer = min(answer, friend_count)

    if answer > len(dist):
        return -1

    return answer
