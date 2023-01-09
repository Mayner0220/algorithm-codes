# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey: list, choices: list) -> str:
    types = ["R", "T", "C", "F", "J", "M", "A", "N"]
    score = {t: 0 for t in types}
    answer = ""

    for s, c in zip(survey, choices):
        if c < 4:
            score[list(s)[0]] += (4 - c)
        else:
            score[list(s)[1]] += (c - 4)

    for type_a, type_b in zip(types[0::2], types[1::2]):
        if score[type_a] > score[type_b]:
            answer += type_a
        elif score[type_a] < score[type_b]:
            answer += type_b
        else:
            answer += sorted([type_a, type_b])[0]

    return answer
