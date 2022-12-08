# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(string: str) -> int:
    alpha_num_dict = {"zero": 0,
                      "one": 1,
                      "two": 2,
                      "three": 3,
                      "four": 4,
                      "five": 5,
                      "six": 6,
                      "seven": 7,
                      "eight": 8,
                      "nine": 9
                      }

    if string.isdigit():
        return int(string)

    temp = ""
    result = ""
    for char in string:
        if char.isdigit():
            result = f"{result}{char}"
        else:
            temp = f"{temp}{char}"

            if temp in alpha_num_dict:
                result = f"{result}{alpha_num_dict[temp]}"
                temp = ""

    return int(result)
