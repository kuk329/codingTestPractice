# 2579번

n= int(input())
s=[0] # index 0 번째 값 (필요없는값)
d=[0]*(n+2)

for _ in range(n):
    s.append(int(input()))

print(s)

d[0]=0
d[1]=s[1]
if n>=2:
    d[2]=s[2]+s[1]

if n>=3:
    for i in range(3,n+1):
        d[i]=max(d[i-1],d[i-3]+s[i-2])+s[i]

print(d)
print(d[n])
