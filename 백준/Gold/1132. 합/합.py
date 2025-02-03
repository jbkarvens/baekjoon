import sys
input=sys.stdin.readline

alp=dict()
first=set()
N=int(input())
for _ in range(N):
    sen=input().strip()
    first.add(sen[0])
    for i,c in enumerate(reversed(sen)):
        if not c in alp:
            alp[c]=0
        alp[c]+=pow(10,i)
alp=sorted(alp.items(),key=lambda x:x[1],reverse=True)
res=0
if len(alp)<10:
    i=9
    for c in alp:
        res+=i*c[1]
        i-=1
else:
    zero=None
    for c in reversed(alp):
        if not c[0] in first:
            zero=c[0]
            break
    i=9
    for c in alp:
        if c[0]==zero:
            continue
        res+=i*c[1]
        i-=1
print(res)