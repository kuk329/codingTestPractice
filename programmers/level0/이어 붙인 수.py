# 정수 배열 -> num_list


def solution(num_list):
    answer = 0
    odd=''
    even=''
    for num in num_list:
        if num%2==0: # 짝수
            even+=str(num)
        else:
            odd+=str(num)

    answer=int(even)+int(odd)
    return answer