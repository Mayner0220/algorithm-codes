# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers: list) -> str:
    num = list(map(str, numbers))
    num.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(num)))
