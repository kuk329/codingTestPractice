# 순차 탐색 : O(n)

def sequential_search(n,target,array):
    # 각 원소 순차적으로 확인
    for i in range(n):
        if array[i]==target:
            return i+1 # index + 1


print("생성할 원소 개수 입력, 찾을 문자열 입력")
input_data= input().split()
n=int(input_data[0])
target=input_data[1]

print("배열에 저장할 문자열 입력")
array=input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n,target,array))


