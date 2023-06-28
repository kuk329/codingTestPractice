
# 자판의 개수는 1부터 최대 100개까지 가능
# 키 하나에 같은 문자가 여러번 할당될수도 있음.
# 아예 할당되지 않은 문자도 있을수 있음. -> 작성할수 없는 문자도 있음.


# 특정 문자열을 작성할 때, 키를 최소 몇번 눌러야 그 문자열을 작성할수 있는지


# keymap : 1번키부터 할당된 문자들이 차례로 담긴 배열
# targets : 입력하려는 문자열이 담긴 배열]]

keymap=["ABACD", "BCEFD"]
targets=["ABCD","AABB"]
d=dict()

result=0

for keys in keymap:
    print(f"keys : {keys}")
    for idx,key in enumerate(keys):
        if key in d:
            before = d[key]
            if d[key]>idx:
                d[key]=idx
        else:
            d[key]=idx+1
        
for target in targets:
    for t in target:
        



# 최소만 구하면 되므로
# {"A":1,"B":1}
