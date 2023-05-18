import sys
sys.setrecursionlimit(10*6)

n=int(input()) # 입력값
d=[-1]*(n+1)



def fibo(n):
    d[0]=0
    d[1]=1
    for i in range(2,n+1):
        d[i]=d[i-1]+d[i-2]

    return d[i]


print(fibo(n))