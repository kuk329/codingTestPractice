
# 완전 탐색 -> 모든 경우의수를 다 확인하는 방법

# 어떤 던전을 먼저 탐험하느냐에 따라 결과가 달라지는데, 최소 피로도와 소모 피로도가 다 다르기때문에 특별한 규칙이 없음.
# (최소 피로도가 낮은것 부터 가야된다 or 소모 피로도가 낮은곳 부터 가야된다 등등)
# 던전의 최대 갯수도 8 이므로 모든 경우의 수를 확인할수있는 완전 탐색으로 진행.

from itertools import combinations, permutations 

def solution(k, dungeons):
    answer = -1
    cnt=0
    stamina=k
    n= len(dungeons)
    for ans in permutations(dungeons,n):
        stamina=k
        cnt=0
        for x,y in ans:
            if stamina>=x:
                stamina-=y
                cnt+=1
        answer = max(cnt,answer)


    return answer





result=solution(80,[[80,20],[50,40],[30,10]])
print(result)