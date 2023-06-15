def solution(a, b, c, d):
    answer = 0
    if a==b==c==d:
        answer=a*1111
    elif a==b==c:
        answer=(10*a+d)*(10*a+d)
    elif b==c==d:
        answer=(10*b+a)*(10*b+a)
    elif a==b==d:
        answer=(10*a+c)*(10*a+c)
    elif a==c==d:
        answer=(10*a+b)*(10*a+b)
    elif a==b and c==d:
        answer=(a+c)*abs(a-c)
    elif a==c and b==d:
        answer=(a+b)*abs(a-b)
    elif a==d and b==c:
        answer=(a+b)*abs(a-b)
    elif a==b and c!=d:
        answer=(c*d)
    elif a==c and b!=d:
        answer=b*d
    elif a==d and b!=c:
        answer=b*c  
    elif b==c and a!=d:
        answer=a*d
    elif b==d and a!=c:
        answer=a*c
    elif c==d and a!=b:
        answer=a*b
    elif a!=b!=c!=d:
        answer = min(a,b,c,d)
        
    return answer
    


