# boolean 변수 x1,x2,x3,x4 가 매개변수로 주어질때, 다음의 식의 true/false를 return 하는 solution함수를 작성
# V : or
# ^ : and


def solution(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    return answer


# ----- sol 2 -------

def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)