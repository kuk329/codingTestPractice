# 2309

# -------- sol 1 ----------- 
# 라이브러리 사용

from itertools import combinations


arr = [int(input()) for _ in range(9)] # 키 9개 입력받음.

total = sum(arr)  # 9명 난쟁이 키 총합

out=[]

for a,b in combinations(arr,2):
    if total-(a+b) == 100:
        out.append(a)
        out.append(b)
        break


arr.sort() # 정렬

for i in range(9):
    if arr[i] not in out:
        print(arr[i])





# -------- sol 2 -----------


arr = [int(input()) for _ in range(9)] # 키 9개 입력받음.

total = sum(arr)  # 9명 난쟁이 키 총합

out=[]


arr.sort() # 정렬


for i in range(8):
    for j in range(i+1,9):
        if total-(arr[i]+arr[j]) == 100:
            out.append(arr[i])
            out.append(arr[j])
            for k in range(9):
                if arr[k] not in out:
                    print(arr[k])
            exit() # 이중 for 문 나오기 위해 


