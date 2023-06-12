# 문자열 배열 : my_strings , 이차원 정수 ㅂㅐ열 :parts

def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        string=my_strings[i]
        s=parts[i][0]
        e=parts[i][1]
        answer+=string[s:e+1]

    return answer



my_strings=["progressive", "hamburger", "hammer", "ahocorasick"]
parts=[[0, 4], [1, 2], [3, 5], [7, 7]]

print(solution(my_strings,parts))