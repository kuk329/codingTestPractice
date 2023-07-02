

def gcd(a,b):# 최대공약수
    while b>0:
        a,b=b,a%b
    return a


def solution(n, m):
    if n<m:
        n,m=m,n
        
    x=gcd(n,m)
    y=n*m//x
    
    
    return [x,y]