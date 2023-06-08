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
    for _ in range(int(input())):
        F=int(input())
        social=myset(2*F)
        names=dict()
        cout=0
        for _ in range(F):
            s1,s2=input().split()
            if s1 not in names:
                names[s1]=cout
                cout+=1
            if s2 not in names:
                names[s2]=cout
                cout+=1
            social.union(names[s1],names[s2])
            print(social.num_element(names[s1]))