import sys
input=sys.stdin.readline
class heap:
    def __init__(self):
        self._list=[None]
        self.N=0
    def add(self,num):
        self.N+=1
        n=self.N
        lst=self._list
        lst.append(num)
        i=n
        while i>1:
            if lst[i]<lst[i//2]:
                lst[i],lst[i//2]=lst[i//2],lst[i]
            else:
                break
            i//=2
    def pop(self):
        if self.N==0:
            return None
        self.N-=1
        n=self.N
        lst=self._list
        m=lst[1]
        k=lst.pop()
        if n==0:
            return m
        lst[1]=k
        i=1
        while True:
            if 2*i+1<=n:
                x=lst[i]
                a,b=lst[2*i],lst[2*i+1]
                if a>=b and x>b:
                    lst[2*i+1],lst[i]=x,b
                    i=2*i+1
                elif a<b and x>a:
                    lst[2*i],lst[i]=x,a
                    i=2*i
                else:
                    break
            elif 2*i==n:
                x,a=lst[i],lst[2*i]
                if a<x:
                    lst[2*i],lst[i]=lst[i],lst[2*i]
                break
            else:
                break
        return m

if __name__=='__main__':
    h=heap()
    for _ in range(int(input())):
        n=int(input())
        if n==0:
            a=h.pop()
            if a is None:
                print(0)
            else:
                print(a)
        else:
            h.add(n)