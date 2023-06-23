# food index 1번부터 

def solution(food):
    answer = ''
    front=""
    for i in range(1,len(food)):
        if food[i]%2!=0:
            food[i]-=1
            
        n=food[i]//2
        front+=str(i)*n
    
    back=front[::-1]
    answer=front+"0"+back
    

    return answer