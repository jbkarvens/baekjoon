import sys
input=sys.stdin.readline
N=int(input())
h=[0]
for _ in range(N):
    h.append(int(input()))
h.append(0)
q=[]
ans=0
for i in range(N+2):
    while len(q)>0 and h[q[-1]]>=h[i]:
        idx=q.pop()
        if len(q)>0:
            ans=max(ans,(i-q[-1]-1)*h[idx])
    q.append(i)
print(ans)