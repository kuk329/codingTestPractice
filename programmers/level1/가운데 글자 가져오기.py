def solution(s):
    answer = ''
    l = len(s)
    if l%2==0:
        answer+=s[l//2-1:l//2+1]
    else:
        answer+=s[l//2]
        
    
    return answer



def solution(s):
    n=len(s)
    half=n//2
  
    return s[half-1:half+1] if n%2==0 else s[half]