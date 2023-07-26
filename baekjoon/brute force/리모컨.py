# 1107 번

n = int(input()) # 이동하려는 채널
m = int(input()) # 고장난 버튼의 개수

broken =[False]*10 # 고장난 버튼과 정상 버튼 구별

if m>0:
    a =list(map(int,input().split()))

else:
    a=[]


for x in a:
    broken[x]=True

def possible(c): # c채널로 이동이 가능하면 그때 c에 있는 숫자 개수
    if c==0: # 이동할 채널이 0번이면
        if broken[0]: # 0번이 고장났으면
            return 0 # 해당 채널로 이동 못함.
        else: # 고장나지 않았으면
            return 1 # 해당 채널로 0 한번 누르고 이동 가능.
    l = 0
    while c>0:
        if broken[c%10]: # 고장난 버튼이 하나라도 있으면 해당 채널로 이동이 불가능 하므로 return 0
            return 0
        l+=1
        c=c//10

    return l # 해당 채널 c 가 예를들어 5457이라고 하면 모든 채널이 고장나지 않았으면 5,4,5,7 네번의 입력만으로 이동이 가능
        

ans = abs(n-100) # 정답의 초기값 설정 -> 모든 이동을 다 +나 - 로만할경우 횟수 저장.

for i in range(0,1000000+1): # 이동할 채널 결정 (모든 방법 다 확인)
    c=i
    l = possible(c) # 해당 채널을 이동할 수 있는지 확인
    if l>0: # 해당 채널로 이동이 가능하다는 뜻
        press = abs(c-n) # c에서 n으로 이동할때 + 나 - 로 이동할수 있는 횟수
        if ans>press+l: # 초기값보다 더 적은 수로 이동할수 있는 경우가 있으면 값을 갱신
            ans =press+l

print(ans)