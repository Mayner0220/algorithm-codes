# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill: str, skill_trees: list) -> int:
    skill_trees = ["".join([s for s in skill_tree if s in skill]) for skill_tree in skill_trees]
    answer = 0

    for skill_tree in skill_trees:
        if skill_tree == skill[:len(skill_tree)]:
            answer += 1

    return answer
