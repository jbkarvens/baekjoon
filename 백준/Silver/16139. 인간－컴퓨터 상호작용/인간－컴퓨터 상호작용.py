import sys
input=sys.stdin.readline
s=input().rstrip()
A=[[0 for _ in range(len(s)+1)] for _ in range(26)]
for i in range(26):
    c=chr(i+ord('a'))
    for j in range(len(s)):
        if s[j]==c:
            A[i][j+1]=A[i][j]+1
        else:
            A[i][j+1]=A[i][j]
for _ in range(int(input())):
    a,l,r=input().split()
    l,r=map(int,[l,r])
    a=ord(a)-ord('a')
    print(A[a][r+1]-A[a][l])