# -------- sol 1 ----------

def solution(myString):
    answer = ''
    tmp='abcdefghijk'
    
    for s in myString:
        if s in tmp:
            answer+='l'
        else:
            answer+=s
    return answer




# -------- sol 2 ----------

def solution(myString):
    answer = [x if x > 'l' else 'l' for x in myString]
    return ''.join(answer)