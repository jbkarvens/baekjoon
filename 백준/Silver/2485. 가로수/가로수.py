import sys
input=sys.stdin.readline
N=int(input())
lst=[]
for _ in range(N):
    lst.append(int(input()))
diff=[]
for i in range(N-1):
    diff.append(lst[i+1]-lst[i])
d=diff[0]
for t in diff:
    a,b=t,d
    while a%b!=0:
        a,b=b,a%b
    d=b
print(sum(diff)//d-len(diff))