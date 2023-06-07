# 11726 번
# 2xn 타일링

# n=int(input())
# d=[0]*(n+1)


# d[1]=1
# d[2]=2
# for i in range(3,n+1):
#     d[i]=d[i-1]+d[i-2]

# print(d[n]%10007)


n=int(input())

d=[0]*(n+1)
d[1]=1
d[2]=2

if n>=3:
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]
        
d[n]=d[n]%10007
print(d[n])