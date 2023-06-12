# 문자열 : my_string, 정수 : n


def solution(my_string, n):
    answer = ''
    answer=my_string[-n:]
    return answer


my_string="ProgrammerS123"
n=11
print(solution(my_string,n))