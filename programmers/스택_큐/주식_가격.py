# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    time = [0] * len(prices)

    for index in range(len(prices) - 1):
        for check in range(index, len(prices) - 1):
            if prices[index] > prices[check]:
                break
            else:
                time[index] += 1

    return time
