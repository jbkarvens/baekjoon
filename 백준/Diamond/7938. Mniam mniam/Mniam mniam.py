import sys
input=sys.stdin.readline

def mobius(n):
    prime_check=[True for _ in range(n+1)]
    mu=[1 for _ in range(n+1)]
    mu[0]=0
    for p in range(2,n+1):
        if prime_check[p]:
            mu[p]=-1
            pp=p*p
            for i in range(p+p,n+1,p):
                prime_check[i]=False
                if i%pp==0:
                    mu[i]=0
                else:
                    mu[i]=-mu[i]
    return mu

if __name__=='__main__':
    mu = mobius(1000010)
    for _ in range(int(input())):
        n,m=map(int, input().split())
        ans = 0
        for d in range(1,max(n,m)+1):
            ans+=mu[d]*((n//d + 1)*(m//d + 1)-1)
        sys.stdout.write(str(ans)+'\n')