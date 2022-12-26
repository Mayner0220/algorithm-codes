# https://school.programmers.co.kr/learn/courses/30/lessons/131128

from collections import Counter


def solution(X: str, Y: str) -> str:
    y_counter = Counter(Y)
    temp = []

    for x_element in X:
        if y_counter[x_element] >= 1:
            y_counter[x_element] -= 1
            temp.append(x_element)
        else:
            del y_counter[x_element]

    if temp:
        if all(t == "0" for t in temp):
            return "0"
        else:
            return "".join(sorted(temp, reverse=True))
    else:
        return "-1"


def solution2(X: str, Y: str) -> str:
    answer = ""

    for num in range(9, -1, -1):
        answer += (str(num) * min(X.count(str(num)), Y.count(str(num))))

    if answer == "":
        return "-1"
    elif len(answer) == answer.count("0"):
        return "0"
    else:
        return answer
