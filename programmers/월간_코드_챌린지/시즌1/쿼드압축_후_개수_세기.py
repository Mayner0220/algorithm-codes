# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]
    arr_length = len(arr)

    def qc(x, y, n):
        set_value = arr[x][y]

        for i in range(x, x+n):
            for m in range(y, y+n):
                if arr[i][m] != set_value:
                    n_div = n // 2

                    qc(x, y, n_div)
                    qc(x, y+n_div, n_div)
                    qc(x+n_div, y, n_div)
                    qc(x+n_div, y+n_div, n_div)

                    return

        answer[set_value] += 1

    qc(0, 0, arr_length)

    return answer
