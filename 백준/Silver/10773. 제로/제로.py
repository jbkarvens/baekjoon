import sys
input=sys.stdin.readline
K=int(input().rstrip())
mystack_=[]
for _ in range(K):
    n=int(input().rstrip())
    if n==0:
        mystack_.pop()
    else:
        mystack_.append(n)
print(sum(mystack_))