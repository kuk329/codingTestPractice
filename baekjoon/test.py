# arr=[12,2,3,4,5]

# new_arr=reversed(arr)
# print(new_arr)

# s='abc'

# new_s = reversed(s)


# a=['a','b','c','d','e']
# print(a[::-1])
# print(a[1:4][::-1])

# k,n = map(int,input().split())
# a = []

# for _ in range(k):
#     a.append(int(input()))
    
# a.sort() # 457 539 743 802

# max_length = 0 # 만들수 있는 최대 길이
# def search(s,e):
#     global max_length
#     while s<=e:
#         cnt=0
#         mid = (s+e)//2
#         for i in range(k): # 해당 길이로 총 랜선을 몇개 만들수 있는지 
#             cnt+=a[i]//mid
#         if cnt<n:
#             e=mid-1
#         else:
#             if max_length<mid:
#                 max_length = mid
#             s=mid+1
#         # elif cnt>n:
#         #     s=mid+1
#         # elif cnt==n: # n개 만들수 있으면
#         #     if max_length<mid:
#         #         max_length=mid
        
             
        

# search(1,a[-1])

# print(max_length)
    
    
 
n,k =map(int,input().split()) # 동전의 개수와, 가치의 합
coins=[]

for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True) # 내림차순
for i in range(0,n):
    cnt=1
    for j in range(i,n):
        while coins[j]<=k:
            k=k-coins[i]
            cnt+=1
            if k==0:
                break
    
        
