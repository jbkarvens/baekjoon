import sys
import random
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def ccw(a,b,c):
    z=(a[0]-b[0])*(c[1]-b[1])-(a[1]-b[1])*(c[0]-b[0])
    if z<0:
        return 1
    elif z>0:
        return -1
    else:
        return 0

def cross(A,B,C,D):
    ab=ccw(A,B,C)*ccw(A,B,D)
    cd=ccw(C,D,A)*ccw(C,D,B)
    if ab==0 and cd==0:
        if A>B: A,B=B,A
        if C>D: C,D=D,C
        
        if A<=D and C<=B:
            return 1
        else:
            return 0
    elif ab<=0 and cd<=0:
        return 1
    else:
        return 0

class myset:
    def __init__(self,n):
        self.N=n
        self.root=[i for i in range(n)]
        self.count=[1 for i in range(n)]
        self.num_disjoint = n
    
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
            self.count[rt_a]+=self.count[rt_b]
            self.num_disjoint -= 1
    
    def num_element(self,a):
        return self.count[self.find(a)]

if __name__=='__main__':
    N = int(input())
    lines=[]
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        lines.append([(x1, y1), (x2, y2)])
    graph = myset(N)
    for i in range(N):
        for j in range(i):
            if cross(*lines[i], *lines[j]):
                graph.union(i, j)
    print(graph.num_disjoint)
    print(max(graph.count))