# n : 음이 아닌 정수

# 음이아닌 정수를 9로 나눈 나머지는 n%9 => 그 정수 n 의 각 자리 숫자의 합을 9 로 나눈 나머지와 같다.


def solution(number):
    answer = 0
    for s in number:
        answer+=int(s)

    answer=answer%9
    return answer


print(solution("78720646226947352489"))



# ---------- sol 2 --------



def solution(number):
    return sum(list(map(int,number)))%9

