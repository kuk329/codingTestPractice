def solution(myString, pat):
    answer = 0
    newString=""
    for s in myString:
        if s=="A":
            newString+="B"
        else:
            newString+="A"
            
    if pat in newString:
        answer=1
    else:
        answer=0
            
    return answer


# ---- other sol --------

def solution(myString,pat):
    return int(''.join([ "A" if i=="B" else "B" for i in pat]) in myString)

