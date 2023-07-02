def solution(a, b):
    answer = 0
    k = len(a)
    for i in range(k):
        answer+=a[i]*b[i]
        
    return answer


def solution(a, b):
    return sum([x*y for x,y in zip(a,b)])