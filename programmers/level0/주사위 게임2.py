# 1 ~ 6 까지 적힌 주사위 3개 
# 각 주사위를 굴려서 나온 숫자 a,b,c
# 세 수가 모두 다르면 a+b+c get
# 두 수만 같으면 (a+b+c) x (a^2 + b^2 + c^2)
# 세 수가 모두 같으면 ..


def solution(a, b, c):
    answer = a+b+c

    if a==b and b==c: # 세 수가 다 같을때
        answer *=(a*a+b*b+c*c)*(a*a*a+b*b*b+c*c*c)
    elif a==b or b==c or a==c: # 두 수만 같을때
        answer *=(a*a+b*b+c*c)

    return answer



# other solution

def solution(a,b,c):
    check = len(set[a,b,c]) # set 이용한 풀이
    if check==1:
        return (a+b+c)*(a**2+b**2+c**2)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        return (a+b+c)

