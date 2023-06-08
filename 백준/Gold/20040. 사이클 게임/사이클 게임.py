import sys
import random
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

class myset:
    def __init__(self,n):
        self.N=n
        self.root=[i for i in range(n)]
        self.count=[1 for i in range(n)]
    
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
    
    def num_element(self,a):
        return self.count[self.find(a)]

if __name__=='__main__':
    n,m=map(int,input().split())
    pair=[]
    game=myset(n)
    for _ in range(m):
        pair.append(list(map(int,input().split())))
    num,iscycle=0,False
    for i in range(m):
        x,y=pair[i]
        if game.find(x)==game.find(y):
            num=i+1
            break
        game.union(x,y)
    print(num)