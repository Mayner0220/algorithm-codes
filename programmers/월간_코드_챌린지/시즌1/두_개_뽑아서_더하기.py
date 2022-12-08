# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers: list) -> list:
    answer = []
    length = len(numbers)

    for i in range(0, length):
        for j in range(i+1, length):
            temp = numbers[i] + numbers[j]

            if temp not in answer:
                answer.append(temp)

    return sorted(answer)
