# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes: list, signs: list) -> int:
    result = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            result += absolute
        else:
            result -= absolute

    return result
