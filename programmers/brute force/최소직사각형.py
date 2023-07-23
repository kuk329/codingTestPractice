
def solution(sizes):
    answer = 0
    rows=[]
    cols=[]
    
    for size in sizes:
        row,col = max(size[0],size[1]),min(size[0],size[1])
        rows.append(row)
        cols.append(col)
    rows.sort()
    cols.sort()
    
    return rows[-1]*cols[-1]

