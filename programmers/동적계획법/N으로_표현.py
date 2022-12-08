# https://school.programmers.co.kr/learn/courses/30/lessons/42895


def solution(N: int, number: int) -> int:
    answer = -1
    dp = []

    for idx in range(1, 9):
        num = {int(str(N) * idx)}

        for check in range(0, idx - 1):
            for x in dp[check]:
                for y in dp[-check - 1]:
                    num.add(x + y)
                    num.add(x - y)
                    num.add(x * y)

                    if y != 0:
                        num.add(x // y)

        if number in num:
            return idx

        dp.append(num)

    return answer
