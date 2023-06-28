def solution(n):
    answer=''
    arr=[int(i) for i in str(n)]
    arr.sort(reverse=True)
    for x in arr:
        answer+=str(x)
        
        
        
    return int(answer)