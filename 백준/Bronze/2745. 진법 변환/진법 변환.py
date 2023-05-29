B,N=input().split()
N=int(N)
sol=0
for i in range(len(B)):
    ltr=B[len(B)-i-1]
    if ord('A')<=ord(ltr)<=ord('Z'):
        ltr=ord(ltr)-ord('A')+10
    else:
        ltr=int(ltr)
    sol+=ltr*N**i
print(sol)