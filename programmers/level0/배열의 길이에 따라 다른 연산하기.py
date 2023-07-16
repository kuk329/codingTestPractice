def solution(arr, n):
    k = len(arr)
    if k%2==0: #짝수
        i=1
        while i<k:
            arr[i]+=n  
            i+=2
    else: 
        i=0
        while i<k:
            arr[i]+=n
            i+=2
        
    return arr