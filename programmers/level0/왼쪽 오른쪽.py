# 문자열 리스트 str_list 

def solution(str_list):
    answer = []
    for idx,s in enumerate(str_list):
        if s=="l":
            answer=str_list[:idx]
            break
        if s=="r":
            answer=str_list[idx+1:]
            break
            
    return answer