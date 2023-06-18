

def solution(number):
    answer = 0
    n=len(number)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if number[i]+number[j]+number[k]==0:
                    answer+=1
            
    return answer


# ---- sol 2 -------

from itertools import combinations

def solution(number):
    answer=0
    n=len(number)
    for i in combinations(number,3):
        if sum(i)==0:
            answer+=1

    return answer