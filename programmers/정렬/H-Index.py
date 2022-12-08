# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations: list) -> int:
    citations.sort()
    citations_cnt = len(citations)
    result = 0

    for idx in range(citations_cnt):
        if citations[idx] >= citations_cnt-idx:
            result = citations_cnt-idx
            break

    return result
