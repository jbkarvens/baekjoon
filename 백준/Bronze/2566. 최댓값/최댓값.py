mat=[]
for _ in range(9):
    mat.append(list(map(int,input().split())))
max_el,u,v=mat[0][0],0,0
for i in range(9):
    for j in range(9):
        if max_el<mat[i][j]:
            max_el,u,v=mat[i][j],i,j
print(max_el)
print(u+1,v+1)