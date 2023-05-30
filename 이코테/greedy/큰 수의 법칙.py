

n,m,k = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort(reverse=True) # 내림차순 정렬

result = 0
count = 0

for _ in range(m):
    if count<k:
        result+=arr[0]
        count+=1
    else:
        count=0
        result+=arr[1]



print(f'결과:  {result}')