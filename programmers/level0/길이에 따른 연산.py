

def solution(num_list):
    answer = 0
    n=len(num_list)
    if n>=11:
        answer=sum(num_list) 
    else:
        answer=1
        for num in num_list:
            answer*=num
    
    return answer



# --- other sol -----

def solution(num_list):
    if len(num_list)>=11:
        return eval('+'.join(list(map(str,num_list))))
    else:
        return eval('*'.join(list(map(str,num_list))))