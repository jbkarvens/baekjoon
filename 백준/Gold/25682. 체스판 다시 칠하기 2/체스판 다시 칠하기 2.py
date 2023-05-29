import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
ls=[]
for _ in range(N):
    ls.append(input().rstrip())
S=[[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if ((i+j)%2==0 and ls[i-1][j-1]=='B') or ((i+j)%2==1 and ls[i-1][j-1]=='W'):
            S[i][j]=S[i][j-1]+1
        else:
            S[i][j]=S[i][j-1]
for i in range(1,N+1):
    for j in range(1,M+1):
        S[i][j]+=S[i-1][j]
ans=K*K
for i in range(N+1-K):
    for j in range(M+1-K):
        tmp=S[i+K][j+K]-S[i][j+K]-S[i+K][j]+S[i][j]
        ans=min(tmp,K*K-tmp,ans)
print(ans)