M=int(input())
N=int(input())
lst=[]
for i in range(M,N+1):
    isPrime=True
    for j in range(2,i):
        if i%j==0:
            isPrime=False
            break
    if isPrime and i>1: lst.append(i)
if len(lst)==0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])