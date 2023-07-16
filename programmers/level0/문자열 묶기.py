def solution(strArr):
    arr=[0 for i in range(31)]
    for s in strArr:
        n=len(s)
        arr[n]+=1
        
    return max(arr)