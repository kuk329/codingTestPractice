def solution(n):
    answer=[int(i) for i in str(n)]
    answer.reverse()
    return answer


def digit_reverse(n):
    return list(map(int, reversed(str(n))))