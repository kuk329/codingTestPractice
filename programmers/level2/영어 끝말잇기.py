
def solution(n, words):
    answer = []
    tmp=[]
    person_num=0
    repeat=0
    answer=[0,0]
    for i in range(len(words)):
        if words[i] in tmp: # 탈락  
            person_num=i%n+1
            repeat = i//n+1
            break
        elif tmp and tmp[-1][-1]!=words[i][0]:
            
            person_num=i%n+1
            repeat = i//n+1
            break
        else:
            tmp.append(words[i]) # 통과

    answer=[person_num,repeat]
 

    return answer



print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))