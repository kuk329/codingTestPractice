from collections import deque

def solution(myStr):
    answer = []
    q=deque(myStr)
    tmp=""
    
    while q:
        x=q.popleft()
        
        if x in "abc":
            if tmp:
                answer.append(tmp)
            tmp=""
        else:
            tmp+=x
      
    
    if tmp:
        answer.append(tmp)
    
    if not answer:
        return ["EMPTY"]
        
    
    return answer


# ----- sol 2 ---------

def solution2(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']



# myStr="cabab"

# arr=myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
# print(arr)

# print(solution2(myStr))