import sys
input=sys.stdin.readline

N=int(input())
arr=list(input().split())
cnt=[[0,chr(ord('A')+i)] for i in range(26)]
for c in arr:
    cnt[ord(c)-ord('A')][0]+=1
cnt.sort(reverse=True)
if cnt[0][0]>(N+1)//2:
    print("NE")
else:
    res=[None]*N
    arr=[]
    for i in range(26):
        arr+=[cnt[i][1]]*cnt[i][0]
    pos=0
    for j in range(2):
        i=j
        while i<N:
            res[i]=arr[pos]
            i+=2
            pos+=1
    print(*res)