import sys
import random
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

class myset:
    def __init__(self,n):
        self.N=n
        self.root=[i for i in range(n)]
    
    def find(self,x):
        if self.root[x]==x:
            return self.root[x]
        self.root[x]=self.find(self.root[x])
        return self.root[x]
    
    def union(self,a,b):
        if random.randint(0,1):
            a,b=b,a
        rt_a=self.find(a)
        rt_b=self.find(b)
        if rt_a!=rt_b:
            self.root[rt_b]=rt_a

if __name__=='__main__':
    N=int(input())
    korea=myset(N)
    m=int(input())
    for i in range(N):
        lst=list(map(int,input().split()))
        for j,t in enumerate(lst):
            if t:
                korea.union(i,j)
    plan=list(map(int,input().split()))
    can_travel=True
    for i in range(len(plan)-1):
        if korea.find(plan[i]-1)!=korea.find(plan[i+1]-1):
            can_travel=False
            break
    print('YES' if can_travel else 'NO')