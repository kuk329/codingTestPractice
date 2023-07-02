# ---- sol 1 -----

def solution(left, right):
    answer = 0
    for n in range(left,right+1):
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count%2==0: #짝수
            answer=answer+n
        else:
            answer=answer-n
    return answer


# ---- sol 2 -----

def solution(left, right):
    answer = 0
    for n in range(left,right+1):
        count=1 # 자기자신
        for i in range(1,n//2+1):
            if n%i==0:
                count+=1
        if count%2==0:
            answer+=n
        else:
            answer-=n
        
    return answer



# ---- sol 3 -------

def solution(left, right):
    answer=0
    for i in range(left,right+1):
        if int(i**0.5)==i**5: # 제곱근이 정수로 나오면 그 수의 약수의 개수는 홀수
            answer-=1
        else:
            answer+=1

    return answer