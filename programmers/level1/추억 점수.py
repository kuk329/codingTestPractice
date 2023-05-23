def solution(name, yearning, photo):
    temp = dict()
    answer = []
    for i in range(len(name)):
        temp[name[i]]=yearning[i]
        
    print(temp)
    for p in photo:
        num=0
        for person in p:
            if person in temp:
                num+=temp[person]
        
        answer.append(num)
    return answer