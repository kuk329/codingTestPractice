def solution(s):
    s=s.lower()
    p=s.count('p')
    y=s.count('y')
    if p==y:
        return True
    else:
        return False




def solution(s):
    answer = True
    countY=0
    countP=0
    for x in s:
        if x=='p' or x=='P':
            countP+=1
        if x=='y' or x=='Y':
            countY+=1
            
    if countP==countY:
        answer=True
    else:
        answer=False

    return answer