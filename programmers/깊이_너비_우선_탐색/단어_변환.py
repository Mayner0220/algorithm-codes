# https://school.programmers.co.kr/learn/courses/30/lessons/43163

answer = 0


def solution(begin: str, target: str, words: list) -> int:
    global answer
    if target not in words:
        return 0

    visited = [False for _ in words]
    dfs(begin, target, words, visited)

    return answer


def dfs(begin: str, target: str, words: list, visted: list) -> int or None:
    global answer
    stack = [begin]

    while stack:
        word = stack.pop()
        if word == target:
            return answer

        for idx in range(len(words)):
            if len([i for i in range(len(words[idx])) if words[idx][i] != word[i]]) == 1:
                if visted[idx] != 0:
                    continue

                visted[idx] = True
                stack.append(words[idx])
        answer += 1
