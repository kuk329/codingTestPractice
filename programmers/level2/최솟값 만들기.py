

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    print(A)
    print(B)
    for i in range(len(A)):
        answer+=A[i]*B[i]
  
    return answer


# ----- other sol ----

def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])