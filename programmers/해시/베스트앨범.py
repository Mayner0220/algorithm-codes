# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres: list, plays: list) -> list:
    answer = []
    genre_total = {}
    genre_dic = {}

    for i in range(len(genres)):
        if genres[i] not in genre_dic.keys():
            genre_dic[genres[i]] = [(plays[i], i)]
            genre_total[genres[i]] = plays[i]
        else:
            genre_dic[genres[i]].append((plays[i], i))
            genre_total[genres[i]] = genre_total[genres[i]] + plays[i]

    sort_play = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)

    for key in sort_play:
        genre_list = genre_dic[key[0]]
        genre_list = sorted(genre_list, key=lambda x: ([-x[0], x[1]]))

        for i in range(len(genre_list)):
            if i == 2:
                break
            answer.append(genre_list[i][1])

    return answer
