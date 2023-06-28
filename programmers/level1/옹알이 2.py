

def solution(babbling):
    answer = 0
    babble=["aya","ye","woo","ma"]
    for word in babbling:
        for text in babble: # 4번 반복
            if text*2 not in word:
                word = word.replace(text," ")
                
        if word.strip()=="":
            answer+=1
            
    return answer
