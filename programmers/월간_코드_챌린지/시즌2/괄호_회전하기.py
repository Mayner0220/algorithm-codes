# https://school.programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque


def solution(s: str) -> int:
    s = deque(s)
    answer = 0

    for _ in range(len(s)):
        stack = []
        idx = 0

        for element in s:
            stack.append(element)
            idx += 1

            if idx >= 2:
                if stack[idx - 2] + stack[idx - 1] in ["[]", "()", "{}"]:
                    del stack[idx - 1]
                    del stack[idx - 2]
                    idx = len(stack)

        if not stack:
            answer += 1

        s.rotate(-1)

    return answer
