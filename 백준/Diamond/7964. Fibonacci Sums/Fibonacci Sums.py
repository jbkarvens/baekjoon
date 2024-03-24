import sys
input=sys.stdin.readline

x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = [0 for _ in range(max(len(x),len(y))+2)]
for i,xx in enumerate(x[1:]):
    z[i]+=xx
for i,yy in enumerate(y[1:]):
    z[i]+=yy


for i in reversed(range(2,len(z))):
    if z[i]==1 and z[i-1]==2:
        z[i+1],z[i],z[i-1]=1,0,1
    elif z[i]==2 and z[i-1]==0:
        z[i+1],z[i]=1,0
        z[i-2]+=1
    elif z[i]==2 and z[i-1]==1:
        z[i+1],z[i],z[i-1]=1,1,0
    elif z[i]==3:
        z[i+1],z[i]=1,1
        z[i-2]+=1
if z[1]==3:
    z[2],z[1],z[0]=1,1,1
if z[1]==2 and z[2]==0:
    z[2],z[1],z[0]=1,0,1
if z[1]==2 and z[2]==1:
    z[3],z[2],z[1],z[0]=1,0,1,0
if z[0]==3:
    z[1],z[0]=1,1
if z[0]==2 and z[1]==1:
    z[2],z[1],z[0]=1,0,1
if z[0]==2 and z[1]==0:
    z[1],z[0]=1,0

for i in range(len(z)-2):
    if z[i]==1 and z[i+1]==1 and z[i+2]==0:
        z[i+2],z[i+1],z[i]=1,0,0
for i in reversed(range(len(z)-2)):
    if z[i+2]==0 and z[i+1]==1 and z[i]==1:
        z[i+2],z[i+1],z[i]=1,0,0
for i in reversed(range(len(z))):
    if z[i]==0:
        z.pop()
    else:
        break
print(len(z),*z,sep=' ')