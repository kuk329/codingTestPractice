

def solution(num_list):
    answer = 0
    for num in num_list:
        while True:
            if num==1:
                break
            if num%2==0:
                num=num//2
            else:
                num-=1
                num=num//2
            answer+=1
    return answer