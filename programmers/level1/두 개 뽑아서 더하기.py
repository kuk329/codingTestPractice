# numbers : 정수 배열 -> 서로 다른 인덱스에 있는 두개 더해서 만들기 -> 조합문제 
# combination or 이중 for문 사용
# nC2

from itertools import combinations

def solution(numbers):
    answer = []
    tmp=set()
    idx=[x for x in range(0,len(numbers))]
    for a,b in combinations(idx,2): # index 조합 생성
        x = numbers[a]+numbers[b]
        tmp.add(x)

    answer=sorted(list(tmp))
        

    return answer