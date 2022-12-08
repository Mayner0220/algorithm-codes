# https://school.programmers.co.kr/learn/courses/30/lessons/42627

def solution(jobs: list) -> int:
    result, start = 0, 0
    length = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])

    while jobs:
        for idx in range(len(jobs)):
            if jobs[idx][0] <= start:
                start += jobs[idx][1]
                result += start - jobs[idx][0]
                jobs.pop(idx)
                break

            if idx == len(jobs)-1:
                start += 1

    return int(result/length)
