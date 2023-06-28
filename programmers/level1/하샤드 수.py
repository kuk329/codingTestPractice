
def solution(x):
    x_str=str(x) # 문자열로 바꿈
    x_list=[int(i) for i in x_str] # 문자열을 모두 쪼개서 정수로 바꿔서 배열
    x_sum=sum(x_list)
    if x%x_sum==0:
        return True
    else :
        return False