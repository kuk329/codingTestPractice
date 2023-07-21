
def solution(people, limit):
    answer = 0
    n = len(people)
    people.sort() # 오른차순 정렬
    weight=0 # 배에 탄 사람의 무게
    boat = 0 # 구명조끼 개수
    cnt=0 # 몇명 탔는지
    for n in people:
        weight+=n
        cnt +=1
        if cnt ==2 or weight>limit:
            boat+=1
            cnt=0
            weight = 0
       


    return boat