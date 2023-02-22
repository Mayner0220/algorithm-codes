# https://school.programmers.co.kr/learn/courses/30/lessons/155652

from string import ascii_lowercase


def solution(s: str, skip: str, index: int) -> str:    
    ascii_set = set(ascii_lowercase)
    ascii_set -= set(skip)
    ascii_set = sorted(ascii_set)
    length = len(ascii_set)    
    alpha_dic = {alpha: idx for idx, alpha in enumerate(ascii_set)}
    return "".join([ascii_set[(alpha_dic[e] + index) % length] for e in s])
