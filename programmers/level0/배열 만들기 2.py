# 정수 l, r
# 0과 5로만 이루어진 정수인지 어떻게 찾을건가
# -> 해당 숫자를 문자열로 만들어서 해당 문자열을 앞에서 부터 읽으면서 0이나 5인지 확인.

def solution(l, r):
    answer = []
    for x in range(l,r+1):
        is_0_5 =True
        tmp=str(x)
        for s in tmp:
            if s=="0" or s=="5":
                pass
            else:
                is_0_5=False
        if is_0_5==True:
            answer.append(x)
    
    if len(answer)>0:
        return answer
    else:
        return [-1]
  
# 파이썬 집합(set) 을 이용한 간단한 풀이
def solution2(l,r):
    answer=[]
    for num in range(l,r+1):
        if not set(str(num))-set(['0','5']):
            answer.append(num)
    return answer if answer else [-1]