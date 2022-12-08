# https://school.programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict


def solution(tickets: list) -> list:
    answer = []
    graph = defaultdict(list)

    for (departure, arrival) in tickets:
        graph[departure].append(arrival)

    for departure_airport in graph.keys():
        graph[departure_airport].sort(reverse=True)

    stack = ["ICN"]
    while stack:
        top = stack.pop()

        if top not in graph or not graph[top]:
            answer.append(top)
        else:
            stack.append(top)
            stack.append(graph[top].pop())

    return answer[::-1]
