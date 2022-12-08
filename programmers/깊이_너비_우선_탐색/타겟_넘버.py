# https://school.programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque


def solution(numbers: list, target: int) -> int:
    result = 0
    stack = deque([(0, 0)])

    while stack:
        current, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current == target:
                result += 1

        else:
            number = numbers[num_idx]
            stack.append((current+number, num_idx+1))
            stack.append((current-number, num_idx+1))

    return result
