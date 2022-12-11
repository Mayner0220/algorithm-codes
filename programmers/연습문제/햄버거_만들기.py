# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient: list) -> int:
    answer = 0
    idx = 0

    while idx < len(ingredient) - 3:
        if ingredient[idx] == 1 and ingredient[idx:idx + 4] == [1, 2, 3, 1]:
            del ingredient[idx:idx + 4]
            answer += 1
            idx -= 3
            continue
        idx += 1
    return answer
