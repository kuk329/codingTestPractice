# 벨만 포드 알고리즘 -> 그래프의 최단 경로 구하기

# 음의 간선이 포함된 경우에도 가능
# 음수 간선의 순환 감지 가능
# 시간 복잡도는 O(VE)로 다익스트라 알고리즘보다 느림

# 동작 순서
# 1. 출발 노드 설정
# 2. 최단 거리 테이블을 초기화한다.
# 3. 다음의 과정을 N-1 번 반복한다.
#  - 전체 간선 E개를 하나씩 확인
#  - 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신

# 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한번 더 수행한다.
# - 이때 최단거리 테이블이 갱신된다면 음수간선 순환이 존재하는 것. 

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n,m = map(int,input().split()) # 노드, 간선 개수 

edges=[] # 모든 간선에 대한 정보를 담는 리스트 만들기

dist = [INF]*(n+1) # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선의 정보 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))


def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start]=0
    # 전체 n번의 라운드 반복
    for i in range(n):
        for j in range(m): # 매 반복마다 모든 간선을 확인
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur]!=INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur]+cost
                if i==n-1: # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                    return True
        return False



# 벨만 포드 알고리즘 수행
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print("-1")
else:
    for i in range(2,n+1):
        if dist[i]==INF:
            print("-1")
        else:
            print(dist[i])