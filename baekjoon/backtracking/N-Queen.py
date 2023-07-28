# 9663번



# x 번째 행에 놓은 queen 에 대해서 검증
def check(x):
    # 이전 행에서 놓았던 모든 퀸들을 확인한다.
    for i in range(x):
        if row[x]==row[i]: # 위쪽 확인
            return False
        if abs(row[x]-row[i])==x-i: # 대각선 확인
            return False
    return True

# x 번째 행에 대하여 처리
def dfs(x):
    global result
    if x==n:
        result +=1
    else:
        # x번째 행의 각 열에 퀸을 둔다고 가정
        for i in range(n):
            row[x]=i
            if check(x): # 실제로 이 위치에 두어도 괜찮은지 확인
                dfs(x+1) # 다음 행으로 넘어감.


n = int(input())
row = [0]*n
result = 0
dfs(0)
print(result)
