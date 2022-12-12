# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k: int, m: int, score: list) -> int:
    score = sorted(score, reverse=True)
    answer = 0

    for idx in range(0, len(score), m):
        temp = score[idx:idx + m]

        if len(temp) == m:
            answer += min(temp) * m
    return answer
