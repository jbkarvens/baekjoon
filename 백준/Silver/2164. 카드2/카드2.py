N=int(input())
lst=list(range(1,N+1))
start=0
killcard=True
while len(lst)-start>1:
    if killcard:
        start+=1
        killcard=not killcard
    else:
        lst.append(lst[start])
        start+=1
        killcard=not killcard
print(lst[start])