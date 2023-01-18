# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements: list) -> int:
    answer = set()
    length = len(elements)
    elements = elements * 2

    for idx1 in range(1, length + 1):
        for idx2 in range(length):
            answer.add(sum(elements[idx1:idx1 + idx2]))

    return len(answer)
