

def solution(my_string, is_suffix):
    answer = 0
    n = len(my_string)

    for i in range(n):
        tmp=my_string[i:]
        if tmp==is_suffix:
            answer=1

    return answer