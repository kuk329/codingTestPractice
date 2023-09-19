# 13913 번
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX=100000

n,k = map(int,input().split())
d=[-1]*(MAX+1) # 방문여부와 시작점으로 부터 해당 지점의 위치 저장
move=[-1]*(MAX+1) # 어느 위치에서 왔는지 이전 위치 저장.


# 모든 위치를 시작 위치에서 가장 빠르게 도착하기 위해서 bfs 사용

def bfs(s):
    d[s]=0 # 시작점은 거리를 0으로 초기화
    move[s]=-1 # 시작점은 이전 위치가 없으므로 -1로 초기화
    q=deque()
    q.append(s)
    while q:
        x=q.popleft()
        if x==k:
            break
        for nxt in [x+1,x-1,x*2]:
            if 0<=nxt<=MAX and d[nxt]==-1: # -1이면 아직 방문을 안했다는 뜻이므로 해당 지점으로 이동 가능.
                q.append(nxt)
                move[nxt]=x # 이전 위치
                d[nxt]=d[x]+1 # 거리 

def go(i): # 재귀로 경로 출력
    if i!=-1:
        go(move[i])
        print(i,end=' ')
  

bfs(n)
print(d[k])
go(k)

