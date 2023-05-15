def recursion(s,l,r):
    if l>=r:
        return 1,1
    elif s[l]!=s[r]:
        return 0,1
    else:
        t,n=recursion(s,l+1,r-1)
        return t,n+1
for _ in range(int(input())):
    s=input().rstrip()
    t,n=recursion(s,0,len(s)-1)
    print(t,n)