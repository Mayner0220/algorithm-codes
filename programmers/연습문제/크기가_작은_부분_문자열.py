# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t: str, p: str) -> int:
    return len([True for idx in range(len(t)-len(p)+1) if int(t[idx:idx+len(p)]) <= int(p)])
