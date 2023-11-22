
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1): # 
    n = int(input())
    arr = list(map(int,input().split()))
    result = 0
    max_num=0
    for val in arr[::-1]:
        if max_num<val:
            max_num=val
        else:
            result+= (max_num-val)
    
            
        
    print(f'#{test_case} {result}')
    
    