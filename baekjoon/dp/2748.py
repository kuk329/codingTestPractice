# 피보나치 수 2
# 피보나치 수 : f(n)=f(n-1)+f(n-2) 식을 사용
# ----- 풀이 1 --------
# dp 이용. -> bottom-up 

n = int(input())
d=[0]*(n+1)
for i in range(n+1):
    if i==0:
        d[i]=0
    elif i==1:
        d[i]=1
    else:
        d[i]=d[i-1]+d[i-2]
        
print(d[n])

# ---- 다른 풀이 -------
# dp 이용. -> top-down

n= int(input())
d=[-1]*(n+1) # or d=[-1]*91
d[0]=0
d[1]=1

def f(x):
    if d[x]==-1:
        d[x] = f(x-1)+f(x-2)
    return d[x]

print(f(n))

# ----- 다른 풀이 -----
# 재귀

n = int(input())

def f(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    return f(n-1)+f(n-2)

print(f(n))
