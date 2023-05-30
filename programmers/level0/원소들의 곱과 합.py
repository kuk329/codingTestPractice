def solution(num_list):
    answer = 0
    ans1=1
    ans2=0
    for num in num_list:
        ans1*=num
        ans2+=num

    ans2=ans2**2

    if ans1<ans2:
        return 1
    else:
        return 0