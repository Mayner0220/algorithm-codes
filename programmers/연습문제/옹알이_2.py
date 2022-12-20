# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling: list) -> int:
    pronunciation = {"aya": "!", "ye": "@", "woo": "#", "ma": "$"}
    replace_list = []
    answer = 0

    for b in babbling:
        for key, value in pronunciation.items():
            b = b.replace(key, value)

        replace_list.append(b)

        for idx in range(len(b) - 1):
            if b[idx] == b[idx + 1]:
                replace_list.remove(b)
                break

    for r in replace_list:
        for s in "!@#$":
            r = r.replace(s, "")

        if r == "":
            answer += 1

    return answer


def solution2(babbling: list) -> int:
    answer = 0
    for b in babbling:
        for p in ["aya", "ye", "woo", "ma"]:
            if p*2 not in b:
                b = b.replace(p, " ")
        if len(b.strip()) == 0:
            answer += 1
    return answer
