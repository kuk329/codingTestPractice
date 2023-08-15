
# -------------- sol 1 --------------

def solution(n):
    a=count_one(n)
    
    while True: # n보다 큰수를 조건에 맞는지 하나씩 확인.
        n+=1
        tmp=count_one(n)
        if tmp==a:
            break
            
    return n
    
    
def count_one(n): # 10진수 n을 2진수로 변환하면서 1의 갯수 저장.
    cnt=0
    while n>1:
        tmp=n%2
        if tmp==1:
            cnt+=1
        n=n//2
    return cnt
    



# -------------- sol 2 --------------    

def solution(n):
    a=bin(n).count('1') # bin 이라는 내장 함수를 통해서 2진수로 변환한뒤(문자열로 바뀜) '1'의 갯수를 센다.
    
    while True:
        n = n+1
        if a ==bin(n).count('1'):
            break

    return n
