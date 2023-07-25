# 1018번

n,m = map(int,input().split()) # n : 세로 , m : 가로

board = [input() for _ in range(n)]
ans = 64

def chess(i,j):
    type1=['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
    type2=['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
    
    cnt1=0
    cnt2=0
    for x in range(8):
        for y in range(8):
            if type1[x][y]!=board[i+x][j+y]:
                cnt1+=1
    
    for x in range(8):
        for y in range(8):
            if type2[x][y]!=board[i+x][j+y]:
                cnt2+=1

    return min(cnt1,cnt2)


# 사용할 체스판 고르기 
for i in range(n):
    for j in range(m):
        if i+8<=n and j+8<=m:
            tmp=chess(i,j)
            if ans>tmp:
                ans=tmp



print(ans)

