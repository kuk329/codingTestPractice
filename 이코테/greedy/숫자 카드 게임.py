

n,m = map(int,input().split())

card = []

for i in range(n):
    card.append(list(map(int,input().split())))


# 모든 행을 돌면서 거기서 가장 작은 숫자를 가져와서 그 숫자들 중에서 가장 큰수 
small=[]

for i in range(n):
    x=min(card[i])
    small.append(x)


#print(small)
result = max(small)
print(f'결과 : {result}')


# --- sol 2 -----
# min 함수 대신 2중 for문을 이용


max_value=0
for i in range(n):
    data = list(map(int,input().split())) # 카드 정보를 따로 저장하지 않고 한줄씩 받아서 바로 그중 최솟값 구하기
    min_value = 10001
    for a in data:
        if min_value>a:
            min_value=a
        
    if max_value<min_value:
        max_value=min_value

print(max_value)

