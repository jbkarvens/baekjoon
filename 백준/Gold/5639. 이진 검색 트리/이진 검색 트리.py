import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

pre=[]
while True:
    try:
        pre.append(int(input()))
    except:
        break
n=len(pre)
post=[]

def work(a,b):
    if a>b or b>=n or a<0:
        return
    root=pre[a]
    i=a+1
    while i<=b and pre[i]<=root:
        i+=1
    work(a+1,i-1)
    work(i,b)
    post.append(root)

work(0,n-1)
for i in range(n):
    print(post[i])