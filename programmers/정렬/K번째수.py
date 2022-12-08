# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array: list, commands: list) -> list:
    answer = []

    for command in commands:
        array_a = array[command[0] - 1:command[1]]
        array_a.sort()
        answer.append(array_a[command[2] - 1])

    return answer
