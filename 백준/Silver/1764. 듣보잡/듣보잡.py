import sys
input=sys.stdin.readline
N,M=map(int,input().split())
a=set()
for _ in range(N):
    a.add(input().rstrip())
b=set()
for _ in range(M):
    b.add(input().rstrip())
lst=sorted(list(a&b))
print(len(lst))
lst.sort()
for name_ in lst:
    print(name_)