N=int(input())
count=0
for _ in range(N):
    lst=[False]*26
    s=list(input())
    test=True
    i,c=0,0
    while i<len(s):
        if s[i]!=c:
            idx=ord(s[i])-ord('a')
            if lst[idx]:
                test=False
                break
            c=s[i]
            lst[idx]=True
        i+=1
    if test : count+=1
print(count)