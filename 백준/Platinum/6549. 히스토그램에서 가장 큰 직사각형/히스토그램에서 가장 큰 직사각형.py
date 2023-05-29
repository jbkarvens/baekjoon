from collections import deque
import math
import sys
input=sys.stdin.readline
MAX_NUM = 10**9+1
class mintree:
    def __init__(self,A):
        n=len(A)
        self.A=A
        self.N=n
        H=math.ceil(math.log2(n))
        self.Tree=[None for _ in range(2**(H+1))]
        self.idxTree=[None for _ in range(2**(H+1))]
        self.init(1,0,n-1)
    def init(self,i,start,end):
        if start==end:
            res=self.A[start]
            self.Tree[i]=res
            self.idxTree[i]=start
            return res,start
        else:
            mid=(start+end)//2
            m1,idx1=self.init(2*i,start,mid)
            m2,idx2=self.init(2*i+1,mid+1,end)
            if m1<=m2:
                self.Tree[i]=m1
                self.idxTree[i]=idx1
                return m1,idx1
            else:
                self.Tree[i]=m2
                self.idxTree[i]=idx2
                return m2,idx2
    def interval_min(self,a,b):
        return self.getmin(1,0,self.N-1,a,b)
    def getmin(self,i,start,end,a,b):
        if end<a or b<start:
            return MAX_NUM,None
        if a<=start and end<=b:
            return self.Tree[i],self.idxTree[i]
        mid=(start+end)//2
        m1,id1=self.getmin(2*i,start,mid,a,b)
        m2,id2=self.getmin(2*i+1,mid+1,end,a,b)
        if m1<=m2:
            return m1,id1
        else:
            return m2,id2
        
while True:
    h=list(map(int,input().split()))
    n=h[0]
    if n==0:
        break
    del h[0]
    S=0
    tree=mintree(h)
    q=deque()
    q.append((0,n))
    while len(q)>0:
        a,b=q.popleft()
        m,c=tree.interval_min(a,b-1)
        S=max(S,m*(b-a))
        if c>a:
            q.append((a,c))
        if b>c+1:
            q.append((c+1,b))
    print(S)