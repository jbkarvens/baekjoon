while True:
    h=list(map(int,input().split()))
    n=h[0]
    if n==0:
        break
    h[0]=-1
    h.append(0)
    q=[]
    S=0
    for i in range(n+2):
        while len(q)>0 and h[q[-1]]>=h[i]:
            j=q.pop()
            w=1
            if len(q)>0:
                w+=q[-1]
            S=max(S,h[j]*(i-w))
        q.append(i)
    print(S)