 # 11399 번

# 가장 시간이 짧게 걸리는 사람부터 먼저 돈을 인출하는 방식이므로 그리디 문제라고 볼수 있다. 
n = int(input())
arr=list(map(int,input().split()))

arr.sort()

d=[0]*n

d[0]=arr[0]
for i in range(1,n):
    d[i]=d[i-1]+arr[i]



print(sum(d))