# 이항 계수 2
# 이항계수 문제는 대표적인 dp 문제이다.

import sys
sys.setrecursionlimit(10**6)

n,k=map(int,input().split())
#dp=[[-1]*(k+1) for i in range(n+1)]
dp=[[0]*1001 for _ in range(1001)]



def bino(n,k):
    if dp[n][k]: # 0이 아닌 수면 값이 이미 있있다는 뜻이므로 그 값을 반환
        return dp[n][k]
    
    if n==k or k==0:
        dp[n][k]=1
    else:
        dp[n][k] = bino(n-1,k-1)+bino(n-1,k)
         
    return dp[n][k]

print(bino(n,k)%10007)

#print(bino(n,k))

# ------- 다른 풀이 --------
# 재귀
# import sys
# sys.setrecursionlimit(10**6)

# n,k=map(int,input().split())

# def recur(n,k):
#     if n==k or k==0:
#         return 1
#     else:
#         return recur(n-1,k-1)+recur(n-1,k)

# print(recur(n,k)%10007)


        
