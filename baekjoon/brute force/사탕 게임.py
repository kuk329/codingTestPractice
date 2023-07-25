n=int(input()) # N 크기

board =[]
result = 0
for i in range(n):
    board.append(list(input()))


# 고른 칸에대한 인접 칸들과 자리 교환
def check(a):
    #n = len(a)
    #print(f'n 값 : {n}')
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if a[i][j] == a[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
        cnt = 1
        for j in range(1, n):
            if a[j][i] == a[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans


for i in range(n):
    for j in range(n):
        # 오른쪽과 교환
        if j+1<n:
            board[i][j],board[i][j+1] = board[i][j+1], board[i][j] # 서로 교환
            temp=check(board)
            if result<temp:
                result = temp
            board[i][j],board[i][j+1] = board[i][j+1], board[i][j]
            
        # 아래쪽과 교환
        if i+1<n:
            board[i][j],board[i+1][j] = board[i+1][j] , board[i][j]
            temp=check(board)
            if result<temp:
                result = temp
            board[i][j],board[i+1][j] = board[i+1][j] , board[i][j]


print(result)