# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book: list) -> bool:
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
