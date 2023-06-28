# numbers : 정수 배열
# n : 정수


def solution(numbers, n):
    answer = 0
    for num in numbers:
        if n <answer:
            break
        answer+=num
        
            
    return answer