n=int(input())
val=[]
for _ in range(n):
    val.append(int(input()))
# 마지막이 2계단일때 점수 최댓값: a/마지막이 1계단: b
a,b=[None for _ in range(n)],[None for _ in range(n)]
a[0],b[0]=0,val[0]
if n>1:
    a[1],b[1]=val[1],val[0]+val[1]
for i in range(2,n):
    a[i]=max(a[i-2],b[i-2])+val[i]
    b[i]=a[i-1]+val[i]
print(max(a[n-1],b[n-1]))