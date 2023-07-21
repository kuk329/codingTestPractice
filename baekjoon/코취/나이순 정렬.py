import sys
input=sys.stdin.readline # 시관 초과 방지


n = int(input()) # 회원 수 입력받음.
info=[]

for _ in range(n):
    age,name = input().split()
    info.append((int(age),name))



# 나이순 정렬 -> 이름순 정렬
info.sort(key=lambda x: x[0])


# 출력
for age,name in info:
    print(age,name)

