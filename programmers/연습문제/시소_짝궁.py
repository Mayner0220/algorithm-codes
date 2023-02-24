# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import defaultdict


def solution(weights: list) -> int:
    answer = 0
    weight_dict = defaultdict(int)
    
    for weight in weights:
        answer += (weight_dict[weight] 
                   + weight_dict[weight/2]
                   + weight_dict[weight*2]
                   + weight_dict[weight*2/3]
                   + weight_dict[weight*3/2]
                   + weight_dict[weight*4/3]
                   + weight_dict[weight*3/4])
        weight_dict[weight] += 1
    return answer
