def solution(arr):
    n=len(arr)
    tmp=1
    cnt=0
    # 1 2 4 8 16 32 ...
    while True: # n 보다 크거나 같은 최소 2의 제곱수 찾기      
        if tmp>=n:
           break    
        cnt+=1
        tmp=2**cnt

    rotat=tmp-n  
    for _ in range(rotat):
        arr.append(0)
      
    return arr

print(solution([1, 2, 3, 4, 5, 6]))
print(solution([58, 172, 746, 89]))