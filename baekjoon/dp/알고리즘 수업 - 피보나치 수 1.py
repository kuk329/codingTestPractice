
n = int(input())
cnt1=0
cnt2=0
def fibo(n):
    global cnt1
    
    if n<2:
        return n
    else:
        cnt1+=1
        return fibo(n-1)+fibo(n-2)
    
    
    
def dp(n):
    global cnt2
    f=[0]*(n+1)
    f[0]=0
    f[1]=1
    f[2]=1
    for i in range(3,n+1):
        f[n]=f[n-1]+f[n-2]
        cnt2+=1

fibo(n)
dp(n)    
print(cnt1,cnt2)
    