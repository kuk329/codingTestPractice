

def solution(array, commands):
    answer = []
    
    for s,e,k in commands:
        tmp=array[s-1:e]
        tmp.sort()
        answer.append(tmp[k-1])
        
    
    return answer