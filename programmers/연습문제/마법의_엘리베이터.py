# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey: int) -> int:
    answer = 0
    storey = [int(num) for num in str(storey)]

    for idx in range(len(storey) - 1, -1, -1):
        if storey[idx] > 5:
            answer += (10 - storey[idx])
            if idx == 0:
                answer += 1
            storey[idx - 1] += 1
        elif storey[idx] == 5 and storey[idx - 1] >= 5 and idx > 0:
            answer += 5
            storey[idx - 1] += 1
        else:
            answer += storey[idx]

    return answer
