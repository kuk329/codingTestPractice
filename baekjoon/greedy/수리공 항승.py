# 딱히 방법 없이 그냥 왼쪽부터 구멍을 매꾸는 방식이므로 greedy

N,L = map(int,input().split())


holes = list(map(int,input().split())) # 구멍 위치 저장
holes.sort()

count = 1 # 필요한 테이프 수 
tmp = holes[0]-0.5+L

for i in range(1,N):
    if holes[i]+0.5<=tmp:
        pass
    else:
        tmp = holes[i]-0.5+L
        count+=1



print(count)
