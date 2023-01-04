# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling: list) -> int:
    answer = 0
    for b in babbling:
        for p in ["aya", "ye", "woo", "ma"]:
            b = b.replace(p, " ")
        if len(b.lstrip()) == 0:
            answer += 1
    return answer
