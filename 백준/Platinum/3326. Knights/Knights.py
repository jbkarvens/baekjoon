import sys
input=sys.stdin.readline
K,N=map(int,input().split())
def turns(x,y,N):
    if x<1 or x>N or y<1 or y>N:
        return 4*N
    if x==N or y==N:
        res=4*N
        for dx,dy in [(-2,-1),(-1,-2),(-2,1),(1,-2)]:
            t=turns(x+dx,y+dy,N)
            res=min(res,t)
        return 1-res if res<=0 else -1-res
    if (x%4==1 or x%4==2) and( y%4==1 or y%4==2):
        return -((x+y-1)//4)*2
    return ((x+y+1)//4)*2-1

ans=[None for i in range(K)]
a=[]
far=0
for _ in range(K):
    a.append(list(map(int,input().split())))
for i in range(K):
    tnow=turns(a[i][0],a[i][1],N)
    if abs(tnow)>abs(far) or (abs(tnow)==far and tnow>0):
        far=tnow
    res=4*N
    ax,ay=0,0
    for dx,dy in [(-2,-1),(-1,-2),(-2,1),(1,-2)]:
        t=turns(a[i][0]+dx,a[i][1]+dy,N)
        if res>t and not(tnow>0 and t>0):
            res=t
            ax,ay=a[i][0]+dx,a[i][1]+dy
    ans[i]=[ax,ay]
if far<0:
    print('NO')
else:
    print('YES')
    for i in range(K):
        print(*ans[i])