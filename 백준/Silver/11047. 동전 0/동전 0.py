N,K=map(int,input().split())
A=[]
for _ in range(N):
    A.append(int(input()))
ans=0
i=1
while K>0:
    ans+=K//A[-i]
    K=K%A[-i]
    i+=1
print(ans)