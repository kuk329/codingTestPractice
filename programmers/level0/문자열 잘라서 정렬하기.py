from collections import deque

def solution(myString):
    answer = []
    q=deque(myString)
    tmp=""
    while q:
        x=q.popleft()
        if x=="x":
            if tmp:
                answer.append(tmp)
            tmp=""
        else:
            tmp+=x
            
    if tmp:
        answer.append(tmp)
            
    answer.sort()
        

    return answer



# --------- sol 2 ---------

def solution(myString):
    return sorted(ch for ch in myString.split('x'))