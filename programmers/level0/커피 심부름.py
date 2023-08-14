# 메뉴 가격만 차이있고 아이스,핫의 가격 차이는 없음.

# 문자열에 특정 문자열이 들어가있는지만 확인

def solution(order):
    answer = 0
    for menu in order:
        if "americano" in menu: 
            answer+=4500
        elif "latte" in menu:
            answer+=5000
        else:
            answer+=4500
    return answer