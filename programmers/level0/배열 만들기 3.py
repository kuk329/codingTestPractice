
def solution(arr, intervals):
    answer = []
    for a,b in intervals:
        for i in range(a,b+1):
            tmp=arr[i]
            answer.append(tmp)
        
    return answer