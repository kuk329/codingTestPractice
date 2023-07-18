# 1181

n = int(input())

words=[]

for _ in range(n):
    word = input()
    words.append(word)

words = list(set(words)) # 중복 단어 제거 

words.sort(key=lambda x: (len(x),x)) # 주어진 조건에 맞게 정렬 


for word in words: # 출력
    print(word)
