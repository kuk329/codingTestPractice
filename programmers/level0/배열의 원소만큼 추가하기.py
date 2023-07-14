
def solution(arr):
    answer = []
    
    for num in arr:
        for _ in range(num):
            answer.append(num)
    return answer


# ---- sol 2 -------

def solution2(arr):
    return [i for i in arr for j in range(i)]


print(solution2([5,1,4]))