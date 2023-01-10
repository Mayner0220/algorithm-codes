# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N: int, stages: list) -> list:
    failure_rate = {stage: 0 for stage in range(1, N + 1)}

    for now in range(1, N + 1):
        challenge = [stage for stage in stages if stage >= now]
        clear = [stage for stage in stages if stage > now]
        failure_rate[now] = 1 - len(clear) / len(challenge) if challenge else 0
        stages = clear

    return sorted(failure_rate, key=lambda x: failure_rate[x], reverse=True)
