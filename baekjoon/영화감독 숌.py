# 딱히 효율적인 풀이가 떠오르지 않으므로 모든 일일이 다 찾아보는 brute force 이용

n = int(input())
title = 666
count=0 # 몇번째 인지 


while True:
    if '666' in str(title):
        count+=1
    if count==n:
        break
    title+=1


print(title)
    
    
