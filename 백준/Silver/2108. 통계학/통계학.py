import sys
input=sys.stdin.readline

N=int(input().rstrip())
lst=list()
for _ in range(N):
    lst.append(int(input().rstrip()))
lst=sorted(lst)
ldict=dict()
for e in lst:
    if e in ldict:
        ldict[e]+=1
    else:
        ldict[e]=1
newlst=list()
for e in ldict:
    newlst.append([e,ldict[e]])
newlst=sorted(newlst,key=lambda x:(-x[1],x[0]))

print(round(sum(lst)/len(lst)))
print(lst[(N-1)//2])
if len(newlst)>1 and newlst[0][1]==newlst[1][1]:
    print(newlst[1][0])
else:
    print(newlst[0][0])
print(lst[N-1]-lst[0])