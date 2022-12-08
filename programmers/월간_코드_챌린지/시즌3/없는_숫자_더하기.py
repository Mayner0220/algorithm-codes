# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers: list) -> int:
    result = 0
    completed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for num in completed_numbers:
        if num not in sorted(numbers):
            result += num

    return result
