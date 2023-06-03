import sys
input=sys.stdin.readline
N=int(input())
h=[]
for _ in range(N):
    h.append(int(input()))
q=[[h[0],1]]
ans=0
for i in range(1,N):
    if q[-1][0]==h[i]:
        ans+=q[-1][1]
        q[-1][1]+=1
        if len(q)>1:
            ans+=1
    elif q[-1][0]>h[i]:
        q.append([h[i],1])
        ans+=1
    else:
        while q and q[-1][0]<h[i]:
            ans+=q[-1][1]
            q.pop()
        if q:
            if q[-1][0]==h[i]:
                ans+=q[-1][1]
                q[-1][1]+=1
                if len(q)>1:
                    ans+=1
            else:
                ans+=1
                q.append([h[i],1])
        else:
            q.append([h[i],1])
print(ans)