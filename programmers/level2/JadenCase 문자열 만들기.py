def solution(s):
    answer = ''
    if s[0].isdigit():
        answer+=s[0]
    else:
        answer+=s[0].upper()
        
    chk=False
    for i in range(1,len(s)):
        if s[i]==" ":
            chk=True
            answer+=s[i]
        else:   
            if chk:
                answer+=s[i].upper()
                chk=False
            else:
                answer+=s[i].lower()
    
    return answer