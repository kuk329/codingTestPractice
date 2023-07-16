def solution(arr1, arr2):
    answer = 0
    n1 = len(arr1)
    n2 = len(arr2)
    if n1>n2:
        answer = 1
    elif n1<n2:
        answer = -1
    else: #same
        sum1=sum(arr1)
        sum2=sum(arr2)
        if sum1>sum2:
            answer = 1
        elif sum1<sum2:
            answer=-1
        else:
            answer = 0
        
        
        
    return answer