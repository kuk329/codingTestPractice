

def solution(n):
    answer = [[] for _ in range(n)]
    print(answer)
    for i in range(n):
        for j in range(n):
            if i==j:
                answer[i].append(1)
            else:
                answer[i].append(0)
    return answer



def solution(n):
    answer=[[0]*n for _ in range(n)]
    for i in range(n):
        answer[i][i]=1
        return answer