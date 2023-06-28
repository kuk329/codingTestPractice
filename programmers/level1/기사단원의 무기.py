
def solution(number, limit, power):
    answer = 0
    divisor=[]
    for n in range(1,number+1):
        count=1 # 약수 개수 
        for i in range(1,n//2+1):
            if n%i==0:
                count+=1
        divisor.append(count)
    
    print(divisor)
    
    for j in range(len(divisor)):
        if divisor[j]>limit:
            answer+=power
        else:
            answer+=divisor[j]   
            
    return answer



print(solution(5,3,2))


print(solution(10,3,2))