# 10815 번

# ----- sol 1 ------- >> binary search 이용

import sys
input = sys.stdin.readline

n = int(input())
cards=[]
match=[]
cards=[int(i) for i in input().split()]

m = int(input())
match=[int(i) for i in input().split()]


cards.sort() # 오름차순 정렬


def find_card(arr,num):
    s = len(arr)
    left=0
    right=s-1
    while left<=right:
        mid=(left+right)//2
        if num==arr[mid]:
            return 1
        elif num<arr[mid]:
            right=mid-1
        else:
            left=mid+1

    return 0


for n in match:
    result=find_card(cards,n)
    print(result,end=' ')


# ----- sol 2 ------- >> 파이썬 dictionary 이용

n = int(input())
cards = [int(i) for i in input().split()]

m = int(input())
checks = [int(i) for i in input().split()]

d=dict()
for i in range(len(cards)):
    d[cards[i]]=0
    
for j in range(m):
    if checks[j] in d:
        print(1,end=' ')
    else:
        print(0,end=' ')