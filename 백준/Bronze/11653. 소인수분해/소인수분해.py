N=int(input())
i=2
while i*i<=N:
    if N%i==0:
        print(i)
        N=N//i
    else:
        i+=1
if N>1:
    print(N)