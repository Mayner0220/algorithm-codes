# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n: int, times: list) -> int:
    length = len(times)
    left_v = 1
    right_v = (length + 1) * max(times)

    while left_v <= right_v:
        mid_v = (left_v + right_v) // 2
        count = 0

        for time in times:
            count += mid_v // time

            if count >= n: break

        if count >= n:
            answer = mid_v
            right_v = mid_v - 1
        elif count < n:
            left_v = mid_v + 1

    return answer
