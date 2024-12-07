import sys
input=sys.stdin.readline

N=int(input())
line=list(input())
V=set()
E=set()
x,y=0,0
V.add((x,y))
for i in range(N):
    c=line[i]
    xx,yy=x,y
    if c=='N':
        x+=1
    elif c=='E':
        y+=1
    elif c=='S':
        x-=1
    elif c=='W':
        y-=1
    else:
        break
    V.add((x,y))
    E.add(((x,y),(xx,yy)))
    E.add(((xx,yy),(x,y)))
print(1-len(V)+len(E)//2)