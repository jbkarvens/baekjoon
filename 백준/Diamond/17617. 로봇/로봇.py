n=int(input())
r,m=map(int,input().split())
x=[*map(int,input().split())]
x.sort()
x.append(m+x[0])
xp=[0 for _ in range(n)]
a=0
for i in range(n):
    xp[i]=x[i+1]-x[i]-2*r
xp+=xp
s=0
for i in range(2*n):
    s+=xp[i]
    s=max(s,0)
    a=max(a,s)
a+=1
print(a//2)