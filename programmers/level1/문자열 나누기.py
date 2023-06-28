
def solution(s):
    answer = 0
    countX=0
    countNotX=0
    first=s[0] # b
    for i in range(0,len(s)):
        if s[i]==first:
            countX+=1 
        else:
            countNotX+=1

        
        if countX==countNotX:
            answer+=1
            if i+1<len(s):
                first=s[i+1]
                countX=0
                countNotX=0  
       
        if countX!=countNotX:
            if i==len(s)-1:
                answer+=1
            
    return answer