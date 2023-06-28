
def solution(absolutes, signs):
    answer = 0
    for idx,num in enumerate(absolutes):
        if signs[idx]==True:
            answer+=num
        else:
            answer-=num
        
    return answer


def solution(absolutes, signs):
    answer=0
    for absolute, sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute


    return answer
