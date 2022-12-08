# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorties: list, location: list) -> int:
    index_arr = [index for index in range(len(priorties))]
    save_arr = priorties.copy()

    i = 0
    while True:
        if save_arr[i] < max(save_arr[i+1:]):
            index_arr.append(index_arr.pop(i))
            save_arr.append(save_arr.pop(i))
        else:
            i += 1

        if save_arr == sorted(save_arr, reverse=True):
            break

    return index_arr.index(location) + 1
