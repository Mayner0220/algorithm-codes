# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums: list) -> int:
    if len(set(nums)) <= len(nums)/2:
        return int(len(set(nums)))
    else:
        return int(len(nums)/2)
