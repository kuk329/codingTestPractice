
def solution(clothes):
    answer = 1
    d = dict()
    for name,type_ in clothes:
        if type_ in d:
            d[type_]+=1
        else:
            d[type_]=1

    for key in d.values():
        answer=answer*(key+1)
           
    answer=answer-1
      
    return answer