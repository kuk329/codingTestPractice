
# my_string : 문자열 , queries : 이차원 정수 배열

# replace : 사용법
# 문자열.replace(old,new,[count]) : old : 바꾸기 전 문자열 , new : 바꿀 문자열 , count :  바꾸고 싶은 길이 
# 원래 문자열 변경이 아닌 바뀐 문자열을 반환


def solution(my_string, queries):
    answer = ''
    for s,e in queries:
        before = my_string[s:e+1]
        after = before[::-1]
        j=0
        for i in range(s,e+1):
            my_string[i]=after[j]
            j+=1


        

    return my_string



my_string = "rermgorpsam"
queries=[[2, 3], [0, 7], [5, 9], [6, 10]]

print(solution(my_string,queries))