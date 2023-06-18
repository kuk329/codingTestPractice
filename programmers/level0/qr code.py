# 두 정수 q,r / 문자열 code 

def solution(q, r, code):
    answer = ''
    n=len(code)
    for i in range(n):
        if i%q==r:
            answer+=code[i]
    return answer


def solution(q, r, code):
    return code[r::q]

