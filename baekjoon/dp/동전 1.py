# 2293 번

# n, k = map(int,input().split())

# coins = []

# for _ in range(n):
#     coins.append(int(input()))


# dp = [0]*(k+1)

# for c in coins: # 초기화
#     if c<=k:
#         dp[c]=1


# for x in range(1,k+1):
#     for y in range(1,x):
#         for coin in coins:
#             if (y+coin)==x:
#                 print(f"x=${x} y=${y} coin=${coin}")
#                 dp[x]=dp[x]+dp[y]

# print(dp)
# print(dp[k])


n, k = map(int, input().split())
coin = []
for _ in range(0, n):
    coin.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for c in coin:
    for i in range(c, k+1):
        dp[i] = dp[i] + dp[i-c]
        print(f"i:{i}, c:{c}, c:{c}, i-c:{i-c}")
        

print(dp)
print(dp[k])