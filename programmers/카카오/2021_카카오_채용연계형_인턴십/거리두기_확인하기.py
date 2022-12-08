# https://school.programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque


def solution(places: list) -> list:
    answer = []

    for place in places:
        flag = 1

        for x in range(5):
            for y in range(5):
                if place[x][y] == "P":
                    result = bfs(place, [x, y, 0])
                    if not result:
                        flag = 0

        answer.append(flag)

    return answer


def bfs(place: list, idx: list):
    queue = deque([idx])
    visited = [[False] * 5 for _ in range(5)]
    ix = [0, -1, 0, 1]
    iy = [-1, 0, 1, 0]

    while queue:
        x, y, d = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + ix[i]
            ny = y + iy[i]
            nd = d + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True

                if place[nx][ny] == "P":
                    if nd <= 2:
                        return False
                elif place[nx][ny] == "O":
                    if nd == 1:
                        queue.append([nx, ny, nd])

    return True
