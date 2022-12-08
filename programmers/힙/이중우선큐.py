# https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations: list) -> list:
    result = []

    for oper in operations:
        command1, command2 = oper.split()

        if command1 == "I":
            result.append(int(command2))
        elif command1 == "D" and len(result)!=0:
            if command2 == "1":
                result.pop(result.index(max(result)))
            else:
                result.pop(result.index(min(result)))

    if len(result) == 0:
        return [0, 0]
    else:
        return [max(result), min(result)]
