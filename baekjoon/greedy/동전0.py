# 동전이 서로 배수 관계이므로 greedy 가능

n,k=map(int,input().split())

# coins=[]

# for _ in range(n):
#     coins.append(int(input()))


coins = [int(input()) for _ in range(n)]



coins.sort(reverse=True)

count = 0


for i in range(n):
    count+=k//coins[i]
    k = k%coins[i]
    

print(count)