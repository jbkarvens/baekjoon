cout=[0,0,0]
def dc(u,v,n):
    c=A[u][v]
    chk=True
    for i in range(n*n):
        if A[u+i//n][v+i%n]!=c:
            chk=False
            break
    if chk:
        cout[c+1]+=1
    else:
        for i in range(9):
            dc(u+(i%3)*(n//3),v+(i//3)*(n//3),n//3)

N=int(input())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
dc(0,0,len(A))
print(cout[0])
print(cout[1])
print(cout[2])