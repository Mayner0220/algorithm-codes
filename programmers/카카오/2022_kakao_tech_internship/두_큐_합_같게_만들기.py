# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque


def solution(queue1: list, queue2: list) -> int:
    queue1, queue2 = deque(queue1), deque(queue2)
    target_sum = (sum(queue1) + sum(queue2)) / 2
    left_sum = sum(queue1)
    answer = 0

    while queue1 and queue2:
        if left_sum > target_sum:
            left_sum -= queue1.popleft()
            answer += 1
        elif left_sum < target_sum:
            element = queue2.popleft()
            left_sum += element
            queue1.append(element)
            answer += 1
        else:
            return answer

    return -1
