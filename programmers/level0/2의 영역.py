

def solution(arr):
    answer = []
    idx=[]
    for i in range(len(arr)):
        if arr[i]==2:
            idx.append(i)
        
    if len(idx)==1:
        x=idx[0]
        answer.append(arr[x])
    if len(idx)>=2:
        s=idx[0]
        e=idx[-1]
        for j in range(s,e+1):
            answer.append(arr[j])
    if len(idx)==0:
        answer.append(-1)
        
    return answer
        

print(solution([1,2,1,4,5,2,9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
        