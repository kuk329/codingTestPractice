
def solution(answers):
    answer = []
    arr1 = [1,2,3,4,5] # 5
    arr2 = [2,1,2,3,2,4,2,5] # 8
    arr3 = [3,3,1,1,2,2,4,4,5,5] # 10
    ans = [0,0,0] # 각 학생별로 맞은 개수 저장. 

    for i in range(len(answers)):
        idx = i%len(arr1)
        if answers[i]==arr1[idx]:
            ans[0]+=1
        idx = i%len(arr2)
        if answers[i]==arr2[idx]:
            ans[1]+=1
        idx = i%len(arr3)
        if answers[i]==arr3[idx]:
            ans[2]+=1   

    max_ = max(ans) # 가장 많이 맞춘 개수 
    
    if max_ == ans[0]: # 누가 가장 많이 맞췄는지 확인
        answer.append(1)
    if max_ == ans[1]:
        answer.append(2)
    if max_ == ans[2]:
        answer.append(3)
    
    return answer