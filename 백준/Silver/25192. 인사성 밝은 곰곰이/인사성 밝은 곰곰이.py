import sys
input=sys.stdin.readline
N=int(input())
keystring_='ENTER'
logset=set()
cout=0
for _ in range(N):
    name_=input().rstrip()
    if name_==keystring_:
        logset=set()
    elif not name_ in logset:
        logset.add(name_)
        cout+=1
print(cout)