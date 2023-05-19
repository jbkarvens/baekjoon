def cout_bin(n):
    B=[None for _ in range(n+2)]
    B[1],B[2]=1,2
    for i in range(3,n+1):
        B[i]=(B[i-1]+B[i-2])%15746
    return B[n]

N=int(input())
print(cout_bin(N))