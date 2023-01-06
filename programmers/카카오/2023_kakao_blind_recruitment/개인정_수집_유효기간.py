# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today: str, terms: list, privacies: list) -> list:
    terms = {term.split()[0]: int(term.split()[1]) * 28 for term in terms}
    today_year, today_month, today_day = map(int, today.split("."))
    answer = []

    for idx, privacy in enumerate(privacies, start=1):
        privacy_year, privacy_month, privacy_day = map(int, privacy.split(" ")[0].split("."))
        category = privacy.split(" ")[1]
        if (today_year - privacy_year) * 12 * 28 + (today_month - privacy_month) * 28 + (today_day - privacy_day) >= \
                terms[category]:
            answer.append(idx)
    return answer
