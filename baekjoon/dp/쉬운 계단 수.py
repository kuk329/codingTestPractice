# 10844번


MOD=1_000_000_000

# dp[n][d] : 길이가 n, 마지막 숫자가 d인 계단수 개수
dp = [[0]*10 for _ in range(101)]

for j in range(1,10): # 초기화
    dp[1][j]=1 

for i in range(2,101):
    for j in range(10):
        if j>0:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

ans = 0

n = int(input())
for j in range(10):
    ans+=dp[n][j]
    ans%=MOD

print(MOD)

