# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number: str, k: int) -> str:
    collected = []

    for (idx, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected += number[idx:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    result = "".join(collected)

    return result
