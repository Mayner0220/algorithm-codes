# https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n: int) -> int:
    result = ""
    while n > 0:
        n -= 1
        result = "124"[n % 3] + result
        n //= 3

    return result
