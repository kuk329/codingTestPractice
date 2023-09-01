
from collections import Counter

def solution(want,number,discount):
    answer = 0
    check={} # 딕셔너리
    for w,n in zip(want,number):
        check[w]=n

    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c==check:
            print(c)
            print(check)
            answer+=1

    return answer



want =["banana", "apple", "rice", "pork", "pot"]
number =[3, 2, 2, 2, 1]
discount =["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

solution(want,number,discount)
