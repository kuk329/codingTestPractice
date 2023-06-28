

def solution(s):
    answer = []
    d=dict() # key: 알파벳 , value : 위치(index)
    for idx,x in enumerate(s):
        if x not in d:
            d[x]=idx
            answer.append(-1)
        else:
            answer.append(idx-d[x])
            d[x]=idx
            
        
    return answer