# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k: int, score: list) -> list:
    answer = []

    for idx in range(1, len(score) + 1):
        if idx <= k:
            answer.append(sorted(score[:idx], reverse=True)[-1])
        else:
            answer.append(sorted(score[:idx], reverse=True)[:k][-1])
    return answer
