# 영어 단어가 적힌 카드 뭉치 2개 받음.
# 규칙을 통해 카드에 적힌 단어들을 사용해 원하는 단어 배열 만들기
# -> 원하는 카드 뭉치에서 카드를 순서대로 한장씩 
# -> 한번 사용한 카드는 다시 사용 x
# -> 카드를 사용하지 않고 다음 카드로 넘어갈수 없음.
# -> 기존 카드 뭉치의 단어 순서는 바꿀수 없음.

def solution(cards1, cards2, goal):
    answer = "Yes"
    x,y=0,0
    for word in goal:
        if len(cards1)>x and cards1[x]==word:
            x+=1
        elif len(cards2)>y and cards2[y]==word:
            y+=1
        else:
            answer="No"
            break
    return answer