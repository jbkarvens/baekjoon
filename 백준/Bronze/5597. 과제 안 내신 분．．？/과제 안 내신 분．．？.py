n,m=30,2
lst=list(range(1,n+1))
for _ in range(n-m):
    lst.remove(int(input()))
for _ in range(m):
    a=min(lst)
    print(a)
    lst.remove(a)