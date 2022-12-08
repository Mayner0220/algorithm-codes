# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s: str) -> list:
    answer = []
    s = s[::-1]
    for idx, letter in enumerate(s):
        find_idx = s.find(letter, idx+1)
        if find_idx != -1:
            answer.append(find_idx-idx)
        else:
            answer.append(find_idx)
    return answer[::-1]
