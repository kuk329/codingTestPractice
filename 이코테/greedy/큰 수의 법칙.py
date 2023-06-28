

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

# --- sol 2 ------
# m 의 수가 엄청 클때 100억 이상일때 빨리 풀수있는 풀이

# n,m,k = map(int,input().split())

# data = list(map(int,input().split()))

arr.sort() # 입력받은 수 오름차순 정렬

first = arr[-1] # 첫번째로 큰 수
second = arr[-2] # 두번째로 큰 수

count = (m//(k+1))*k + m%(k+1) # 첫번째 수의 총 개수

result = count*first # 첫번째 수의 개수 * 첫번째 수
result = result + (m-count)*second # 두번째로 큰 수 개수 * 두번째 수

print(result)
