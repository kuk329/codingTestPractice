# my_string : 문자열 , s,e : 정수

def solution(my_string, s, e):
    answer = ''
    tmp = my_string[s:e+1]
    _tmp = tmp[::-1]
    
    answer=my_string[:s]+_tmp + my_string[e+1:]
    return answer