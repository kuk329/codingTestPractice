# 두 정수 a,d / 길이가 n 인 boolean 배열 included 
# 첫째항 a , 공차 d 



def solution(a, d, included):
    answer = 0
    arr=[a]
    if included[0]==True:
        answer+=arr[0]
    
    for i in range(1,len(included)):
        arr.append(a+d*i)
        if included[i]:
            answer+=arr[i]

    return answer



result=solution(3,4,[True,False,False,True,True])
print(result)

result=solution(7,1,[False,False,False,True,False,False,False])
print(result)