

def solution(arr, flag):
    answer = []
    for a,b in zip(arr,flag):
        if b==True:
            for _ in range(a*2):
                answer.append(a)
        else:
            for _ in range(a):
                answer.pop()
                
    return answer