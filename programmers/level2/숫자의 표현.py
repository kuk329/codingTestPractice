# 우선 연속된 숫자들은 해당 수보다는 작아야되고 2로 나누어 떨어지지 않으면 몫과 몫에 1을 더한 수는 무조건 해당수 
# 짝수면 +1, 홀수면 +2
def solution(n):
    check = -1 # 0 : 짝수 , 1 : 홀수

    if n%2==0: # 짝수
        check = 0
    else:
        check = 1
    
    cnt=0
    tmp=0
    for i in range(1,n//2):
        for j in range(i,n//2):
            tmp+=j # 연속된 숫자의 합
            if tmp==n:
                cnt+=1
                break
            
            if tmp>n:
                break

        
    if check==0:
        cnt+=1
    else:
        cnt+=2
    
    # 예외 처리 
    if n==1:
        cnt=1

    return cnt

  

  # ---- sol 2 ----------
def solution2(num):
    answer = 0
    for i in range(1,num+1): # 시작 숫자를 증가
        summ = 0
        while(summ<num): # 연속된 숫자 더함
            summ+=i
            i+=1
        if summ == num:
            answer+=1 
    return answer
