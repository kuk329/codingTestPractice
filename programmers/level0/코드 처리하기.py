
# 문자가 1이면 mode 변경
# mode 종류는 0 과 1 두개만 존재
# mode에 따라 code를 읽는 방법이 다름 하지만 결과적으로는 ret 라는 문자열을 만드는게 목표

# mode 0 일때
# - idx가 짝수일때만 ret의 맨 뒤에 code[idx] 추가


# mode 1 일때
# - idx가 홀수일때만 ret의 맨 뒤에 code[idx] 추가

# 시작 mode 는 0




def solution(code):
    answer=''
    n = len(code); # 문자열 길이 

    mode = 0
    for idx in range(n):
        if code[idx]=="1":
            if mode==1:
                mode=0
            else:
                mode=1
        else:
            if mode==0:
                if idx%2==0:
                    answer+=code[idx]
            
            if mode==1:
                if idx%2!=0:
                    answer+=code[idx]

    if answer =='':
        return "EMPTY"
    
    return answer