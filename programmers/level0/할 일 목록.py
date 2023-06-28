# todo_list : 문자열 배열
# finished : boolean 배열

def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if finished[i]==False:
            answer.append(todo_list[i])
    return answer