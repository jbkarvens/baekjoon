for _ in range(int(input())):
    k=int(input())
    n=int(input())
    a,b=1,1
    for i in range(n-1):
        a*=(k+i+2)
        b*=(i+1)
    print(a//b)