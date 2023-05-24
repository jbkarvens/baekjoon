NUM=10**9+7
comb=[[None for k in range(n+1)] for n in range(1000+2)]
for n in range(1000+2):
    comb[n][0]=1
    comb[n][-1]=1
for n in range(2,1000+2):
    for k in range(1,n):
        comb[n][k]=comb[n-1][k-1]+comb[n-1][k]
n,p=map(int,input().split())
S=[None for _ in range(p+1)]
S[0]=n
for i in range(1,p+1):
    result=pow(n+1,i+1,NUM)-1
    for j in range(i):
        result-=comb[i+1][j]*S[j]
    result=(result*pow(i+1,-1,NUM))%NUM
    S[i]=result
print(S[p])