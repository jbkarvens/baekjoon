import sys
import random
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def getroot(x):
    if x==root[x]:
        return x
    root[x]=getroot(root[x])
    return root[x]

n,m=map(int,input().split())
root=[None for _ in range(n+1)]
for i in range(n+1):
    root[i]=i
for _ in range(m):
    tag,a,b=map(int,input().split())
    if random.randint(0,1):
        a,b=b,a
    a_root=getroot(a)
    b_root=getroot(b)
    if tag==0 and a_root!=b_root:
        root[b_root]=a_root
    elif tag==1:
        if a_root==b_root:
            print('yes')
        else:
            print('no')