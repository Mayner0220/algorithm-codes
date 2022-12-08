# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos: list, win_nums: list) -> list:
    for num in lottos:
        if num in win_nums:
            win_nums.remove(num)

    highest = len(win_nums) + 1 - lottos.count(0)
    if highest > 6:
        highest -= 1
    elif highest < 1:
        highest += 1

    lowest = len(win_nums) + 1
    if lowest > 6:
        lowest -= 1
    elif lowest < 1:
        lowest += 1

    return [highest, lowest]
