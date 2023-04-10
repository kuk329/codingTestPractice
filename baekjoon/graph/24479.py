#알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(10**6) # M값 범위때문에 재귀호출 제한이 걸릴수 있으므로 라이브러리 이용
input=sys.stdin.readline

N,M,R=map(int,input().split())

arr=[[] for _ in range(N+1)]
order=[0]*(N+1) # 방문 확인과 방문 순서 저장
cnt=1 # 방문 순서 count

for _ in range(M):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for e in arr: # 오름차순 정렬
    e.sort()

def dfs(s):
    global cnt
    order[s]=cnt # 방문 순서 저장
    cnt+=1
    for v in arr[s]:
        if order[v]==0:
            dfs(v)

dfs(R)

for i in range(1,N+1):
    print(order[i])