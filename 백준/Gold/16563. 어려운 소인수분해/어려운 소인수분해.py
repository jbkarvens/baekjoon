M=5000000
N=int(input())
prime_lst=[[] for i in range(M+1)]
for p in range(2,M+1):
    if len(prime_lst[p])==0:
        i=p
        while i<=M:
            prime_lst[i].append(p)
            j=i+i
            while j<=M:
                prime_lst[j].append(p)
                j+=i
            i*=p
lst=list(map(int,input().split()))
for i in lst:
    print(*prime_lst[i])