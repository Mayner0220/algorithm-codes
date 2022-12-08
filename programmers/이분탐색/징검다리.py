# https://school.programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance: int, rocks: list, n: int) -> int:
    answer = 0
    left, right = 0, distance

    rocks.sort()
    rocks.append(distance)

    while left <= right:
        now = 0
        remove_cnt = 0
        mid = (left + right) // 2
        min_distance = float("inf")

        for rock in rocks:
            diff = rock - now

            if diff < mid:
                remove_cnt += 1
            else:
                now = rock
                min_distance = min(min_distance, diff)

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer
