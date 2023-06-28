

# 순서 : 빵 야채 고기 빵
#     : 1  2  3   1

#  ----- 시간 초과 에러 --------
# def solution(ingredient):
#     answer = 0
#     tmp=''
#     order='1231'
#     for i in ingredient:
#         tmp+=str(i)  

#     print(f'tmp:{tmp}') 

#     while True:
#         if order not in tmp:
#             break
#         if order in tmp:
#             tmp=tmp.replace(order,"",1)
#             answer+=1
#             print(f"change:{tmp}")
#             print(f"answer:{answer}")
          
#     return answer



# ---- good solution -----

def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            print(f"s : {s}")
            cnt += 1
            for _ in range(4):
                s.pop()
    return cnt

print(solution( [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]))