def solution(sentence):
    answer = False
    arr=[]
    if sentence[0]==")":
        return False
        
    for s in sentence:
        if s=="(":
            arr.append("(")
        else:
            if len(arr)>=1:
                arr.pop()
            else:
                return False
            
    if len(arr)!=0:
        return False
        

    return True