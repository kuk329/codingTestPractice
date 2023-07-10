def solution(myString):
    answer = []
    count=0
    for s in myString:
        if s=="x":
            answer.append(count)
            count=0
        
        else:
            count+=1
            
    if s=="x":
        answer.append(0)
    else:
        answer.append(count)
    return answer


# ---- other sol ------

def solution(myString):
    return [len(w) for w in myString.split('x')]