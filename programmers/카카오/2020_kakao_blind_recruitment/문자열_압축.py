# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(string: str) -> int:
    results = []

    if len(string) == 1:
        return 1

    for idx1 in range(1, (len(string)//2+1)):
        compression = ""
        temp = string[:idx1]
        cnt = 1

        for idx2 in range(idx1, len(string), idx1):
            if temp == string[idx2:idx1+idx2]:
                cnt += 1
            else:
                if cnt == 1:
                    compression = f"{compression}{temp}"
                else:
                    compression = f"{compression}{cnt}{temp}"

                temp = string[idx2:idx1+idx2]
                cnt = 1

        if cnt == 1:
            compression = f"{compression}{temp}"
        else:
            compression = f"{compression}{cnt}{temp}"

        results.append(len(compression))

    return min(results)
