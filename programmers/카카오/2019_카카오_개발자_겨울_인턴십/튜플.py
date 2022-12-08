# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s: str) -> list:
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s = sorted(s, key=len)

    for nums in s:
        split_nums = nums.split(",")
        for num in split_nums:
            if int(num) not in answer:
                answer.append(int(num))

    return answer