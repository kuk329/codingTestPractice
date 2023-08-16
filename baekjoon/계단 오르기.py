# 2579 번
import sys
input = sys.stdin.readline

n = int(input()) # 계단의 수

s =[0] 

for _ in range(n):
    s.append(int(input()))


d=[0]*(n+1)  # d[i] : i번째 계단까지 오르는데 가장 큰 점수 저장.

d[0]=0
d[1]=s[1]

if n<=2:
    print(sum(s))
else:
    d[2]=s[1]+s[2]
    for i in range(3,n+1):
        d[i]=max(d[i-3]+s[i-1],d[i-2])+s[i]
    print(d[n])


# s =[] 

# for _ in range(n):
#     s.append(int(input()))


# d=[0]*(n)  # d[i] : i번째 계단까지 오르는데 가장 큰 점수 

# d[0]=s[0]
# d[1]=s[0]+s[1]

# if n<=2:
#     print(d(n-1))
# else:
#     for i in range(2,n):
#         d[i]=max(d[i-3]+s[i-1],d[i-2])+s[i]
#     print(d[n-1])

