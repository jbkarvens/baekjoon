import sys
input=sys.stdin.readline

def mobius(n):
    prime_list = [True for _ in range(n+1)]
    mobius_list = [1 for _ in range(n+1)]
    mobius_list[1]=1
    for p in range(2,n+1):
        if prime_list[p]:
            mobius_list[p]=-1
            for i in range(p+p,n+1,p):
                prime_list[i]=False
                if (i//p)%p!=0:
                    mobius_list[i]=-mobius_list[i]
                else:
                    mobius_list[i]=0
    return mobius_list

if __name__=="__main__":
    NUM=50000
    mu = mobius(NUM)
    mu_sum = [0 for _ in range(NUM+1)]
    for i in range(1,NUM+1):
        mu_sum[i]=mu_sum[i-1]+mu[i]
    for _ in range(int(input())):
        a,b,d=map(int,input().split())
        result = 0
        ad=a//d
        bd=b//d
        k_before=0
        k = 1
        while k<=min(ad,bd):
            result+=(mu_sum[k]-mu_sum[k_before])*(ad//k)*(bd//k)
            n=a//(k+1)
            m=b//(k+1)
            if n==0 or m==0:
                break
            k_before=k
            k=min(a//n,b//m)
        sys.stdout.write(f"{result}\n")