import sys
input=sys.stdin.readline

luck=[4,7]
cur=[4,7]
for _ in range(11):
    lst=[]
    for n in cur:
        lst.append(int('4'+str(n)))
        lst.append(int('7'+str(n)))
    for n in lst:
        luck.append(n)
    cur=lst
luck.sort()
cur=set(luck)
veryluck=luck[:]
while cur:
    lst=set()
    for m in cur:
        for n in luck:
            x=m*n
            if x<=10**12:
                lst.add(x)
            else:
                break
    cur=lst
    for x in lst:
        veryluck.append(x)
veryluck=list(set(veryluck))
veryluck.sort()

def find(C):
    left=0
    right=len(veryluck)-1
    if veryluck[left]>C:
        return 0
    if veryluck[right]<=C:
        return right+1
    while left<=right:
        mid=(left+right)//2
        if veryluck[mid]<=C:
            left=mid+1
        else:
            right=mid-1
    return left

for _ in range(int(input())):
    A,B=map(int, input().split())
    print(find(B)-find(A-1))
