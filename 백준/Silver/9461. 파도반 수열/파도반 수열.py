def P(N):
    lst=[None,1,1,1,2,2]
    for i in range(6,N+1):
        lst.append(lst[i-1]+lst[i-5])
    return lst[N]

for _ in range(int(input())):
    N=int(input())
    print(P(N))