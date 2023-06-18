

def solution(my_string, is_prefix):
    answer = 0
    n = len(is_prefix)
    m = len(my_string)
    if m<n:
        return 0
        
    for i in range(n):
        if my_string[i]==is_prefix[i]:
            answer=1
        else:
            answer=0
            break
        
        
    return answer