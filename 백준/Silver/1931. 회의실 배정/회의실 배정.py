import sys
input=sys.stdin.readline
A=[]
for _ in range(int(input())):
    A.append(list(map(int,input().split())))
A=sorted(A,key=lambda x:(x[1],x[0]))
ans,t=1,A[0][1]
for i in range(1,len(A)):
    if A[i][0]>=t:
        ans+=1
        t=A[i][1]
print(ans)