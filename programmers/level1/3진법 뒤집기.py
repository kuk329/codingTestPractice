# def solution(n):
#     result=0
#     th = []
#     while n>0: #3진법으로 변환
#         th.append(n % 3)
#         n = n // 3

#     th.reverse()
#     print(th)
#     #3진법 -> 10진법으로 변환
#     for i in range(len(th)):
#         result+=pow(3,i)*th[i]
#     return result

# print(solution(45))

def solution(n):
    tmp=''
    while n:
        tmp+=str(n%3)
        n=n//3

    print(tmp)
    answer = int(tmp,3)
    return answer

print(solution(45))