def solution(price, money, count):
    # for i in range(1,count):
    #     sum+=money*i
    add=sum(range(1,count+1))
    total=add*price
    diff= money-total
    if diff>0:
        return 0
    else:
        return -diff

def solution(price, money, count):
    answer = -1
    give=0
    for i in range(1,count+1):
        give+=price*i
        
    
    if give>money:
        return give-money
    else:
        return 0




def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)