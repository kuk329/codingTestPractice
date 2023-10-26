from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    
    for city in cities:
        tmp=city.lower() # 소문자로 바꾼 값을 tmp에 저장.
        if tmp in q: # 캐시에 있으면
            answer+=1
            q.remove(tmp) # 있는 정보 삭제하고
            q.append(tmp) # 맨 뒤에 다시 삽입
        else: # 캐시에 없으면
            answer+=5
            if cacheSize==0: # 캐시가 0일경우 계속 miss
                continue

            if len(q)<cacheSize: # 캐시가 다 차지 않았으면
                q.append(tmp) # 그냥 추가
            else: # 캐시가 다 찼으면
                q.popleft() # 삭제하고
                q.append(tmp) # 추가
    return answer


