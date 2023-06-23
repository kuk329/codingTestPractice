


def solution(arr, query):
    for i in range(len(query)):
        idx=query[i]
        if i%2==0: #짝수  
            arr=arr[0:idx+1]
    
        else:
            arr=arr[idx:]
        
    
    return arr


print(solution([0,1,2,3,4,5],[4,1,2]))