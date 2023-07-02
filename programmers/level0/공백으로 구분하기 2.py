


# --- other sol -----

solution=lambda x:x.split()

print(solution(" i    love  you"))

# --- other sol -----

def solution(my_string):
    answer = []
    my_string=my_string.strip()
    check=False
    tmp=""
   
    for s in my_string:
        if s==" ":
            if tmp!="":
                answer.append(tmp)
            tmp=""
            check=True # 빈공간 있다는 뜻
        else:
            tmp+=s
            if check:
                check=False
                
    answer.append(tmp)
            
            
    return answer

