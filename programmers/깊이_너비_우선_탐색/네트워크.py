# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n: int, computers: list) -> int:
    answer = 0
    visited = [False for _ in range(n)]

    for com in range(n):
        if not visited[com]:
            dfs(n, computers, com, visited)
            answer += 1

    return answer


def dfs(n: int, computers: list, com: int, visited: list) -> None:
    visited[com] = True

    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if not visited[connect]:
                dfs(n, computers, connect, visited)
