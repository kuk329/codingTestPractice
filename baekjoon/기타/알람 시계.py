# 2884 번

H,M = map(int,input().split())



m=M-45
h = H
if m<0:
    m=60+m
    h=H-1
    if h<0:
        h=23

print(h,m)

# H, M = map(int, input().split())

# if M < 45 :	# 분단위가 45분보다 작을 때 
#     if H == 0 :	# 0 시이면
#         H = 23
#         M += 60
#     else :	# 0시가 아니면 (0시보다 크면)
#         H -= 1	
#         M += 60
        
# print(H, M-45)	