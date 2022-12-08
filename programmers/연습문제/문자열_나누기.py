# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s: str) -> int:
    x = s[0]
    x_cnt = 0
    x_not_cnt = 0
    split_cnt = 0

    for s_element in s:
        if x is None:
            x = s_element

        if x == s_element:
            x_cnt += 1
        else:
            x_not_cnt += 1

        if x_cnt == x_not_cnt:
            x = None
            x_cnt = 0
            x_not_cnt = 0
            split_cnt += 1

    if x is not None:
        split_cnt += 1

    return split_cnt
