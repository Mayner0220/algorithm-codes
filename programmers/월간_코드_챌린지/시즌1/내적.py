# https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a: list, b: list) -> int:
    return sum([x1*x2 for (x1, x2) in zip(a, b)])
