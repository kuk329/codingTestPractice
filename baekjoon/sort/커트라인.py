# 25305

n , k = map(int,input().split())

score = [i for i in map(int,input().split())]
# score = list(map(int,input().split()))

score.sort()

print(score[-k])