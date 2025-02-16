N=int(input())
mod=10007
res=0

def nCr(n,r):
    x=1
    for i in range(n-r+1,n+1):
        x*=i
    for i in range(1,r+1):
        x//=i
    return x

i=1
while i*4<=N:
    res+=nCr(13,i)*nCr(52-4*i,N-4*i)*pow(-1,i+1)
    res%=mod
    i+=1
print(res)