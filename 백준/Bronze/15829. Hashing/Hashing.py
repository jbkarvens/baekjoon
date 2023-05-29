r=31
M=1234567891
L=int(input())
s=input().rstrip()
h=0
rm=1
for i in range(L):
    h=(rm*(ord(s[i])-ord('a')+1)+h)%M
    rm*=r
print(h)