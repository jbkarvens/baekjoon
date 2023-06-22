import sys
input=sys.stdin.readline

if __name__=='__main__':
    n,m,k=map(int, input().split())
    res=[]
    for _ in range(k):
        f,d=map(int,input().split())
        res.append(m+1-d+f)
    score=10**6
    win=None
    for i in range(k):
        if score>res[i]:
            win=i
            score=res[i]
    print(win+1)