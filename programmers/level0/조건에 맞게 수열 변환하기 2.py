

def solution(arr):
    answer = 0
    n=0
    while n<10:
        new=[]
        for num in arr:
            if num>=50 and num%2==0:
                new.append(num//2)
            elif num<50 and num%2!=0:
                new.append(num*2+1)
            else:
                new.append(num)
    

        if arr==new:
            break
        else:
            answer+=1
            arr=new.copy()
        n+=1


    return answer

    
print(solution([1, 2, 3, 100, 99, 98]))

  