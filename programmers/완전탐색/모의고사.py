# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers: list) -> list:
    answer = []

    solver1 = [1, 2, 3, 4, 5]
    solver2 = [2, 1, 2, 3, 2, 4, 2, 5]
    solver3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for index in range(len(answers)):
        if solver1[index % len(solver1)] == answers[index]:
            scores[0] += 1

        if solver2[index % len(solver2)] == answers[index]:
            scores[1] += 1

        if solver3[index % len(solver3)] == answers[index]:
            scores[2] += 1

    for winner, score in enumerate(scores):
        if score == max(scores):
            answer.append(winner+1)

    return answer
